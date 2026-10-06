"""Verify the distributed research-data package with Python's standard library.

MIT License
Copyright (c) 2026 Yishu Li, Yan Gao and Yongjian Li
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions: the above copyright notice and this
permission notice shall be included in all copies or substantial portions.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR ITS USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from pathlib import Path
import csv, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    with (ROOT/'data'/name).open(newline='',encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def seconds(text):
    h,m,s=text.split(':');return int(h)*3600+int(m)*60+float(s)

with (ROOT/'manifest-sha256.csv').open(newline='') as f:
    manifest=list(csv.DictReader(f))
listed=set()
for row in manifest:
    p=(ROOT/row['path']).resolve()
    assert p.is_relative_to(ROOT) and p.is_file(),row['path']
    assert p.stat().st_size==int(row['bytes']),row['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['path']
    listed.add(row['path'])
actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts and p.name!='manifest-sha256.csv'}
assert actual==listed,(actual-listed,listed-actual)
inventory=read('03_corpus_inventory.csv');cases=read('05_contrastive_case_summaries.csv')
windows=read('06_selected_source_windows.csv');excerpts=read('07_selected_evidence_excerpts.csv')
ids={r['case_id'] for r in inventory};pids={r['passage_id'] for r in windows}
assert len(inventory)==len(ids)==59
assert all(r['analytic_status']=='included' and r['source_access']=='restricted' for r in inventory)
assert len(cases)==len({r['case_id'] for r in cases})==20
assert {r['case_id'] for r in cases}=={r['case_id'] for r in inventory if r['contrastive_anchor_status']=='yes'}
assert len(windows)==len(pids)==len(excerpts)==19
assert pids=={f'P{i:02d}' for i in range(1,20)}=={r['passage_id'] for r in excerpts}
assert len({r['case_id'] for r in windows})==10
assert len(read('04_operational_definitions.csv'))==18
assert all(r['case_id'] in ids for rows in [cases,windows,excerpts] for r in rows)
lookup={r['passage_id']:r for r in windows}
for e in excerpts:
    w=lookup[e['passage_id']];assert w['case_id']==e['case_id']
    marks=re.findall(r'(?m)^(\d\d:\d\d:\d\d\.\d+) \[([^\]]+)\]$',e['selected_english_excerpt'])
    assert marks,e['passage_id']
    assert all(seconds(w['working_record_start'])<=seconds(t)<seconds(w['working_record_end_exclusive']) for t,tag in marks)
    if e['case_id']=='#14':assert all(tag=='SPEAKER_2' for t,tag in marks)
    if e['passage_id'] in ['P12','P16','P17']:assert all(tag=='SPEAKER_0' for t,tag in marks)
for row in read('08_finding_evidence_map.csv'):
    assert all(x.strip() in pids for x in row['passage_ids'].split(';'))
    assert all(x.strip() in ids for x in row['comparison_case_ids'].split(';'))
assert len(re.findall(r'^### Q\d+$',(ROOT/'instruments/02_interview_guide_english.md').read_text(),re.M))==16
text='\n'.join((ROOT/rel).read_text() for rel in listed if not rel.startswith('scripts/'))
for banned in ['9ncmx36nwd','Institutionalised Multilingual Development','goto{','/Users/','source_file_path','Su Su','Guangzhou','Zhuhai','Thai students','Thailand']:
    assert banned.casefold() not in text.casefold(),banned
for p in (ROOT/'data').glob('*.csv'):
    for r in list(csv.reader(p.open(newline='',encoding='utf-8'))):
        assert not any(c.lstrip().startswith(('=','+','@')) for c in r),p.name
print(json.dumps({'ok':True,'files_checked':len(manifest),'corpus':59,'contrastive_cases':20,'source_windows':19,'source_cases':10,'definitions':18,'finding_map_rows':4,'interview_questions':16,'raw_sources_included':False},indent=2))
