# Data dictionary

CSV files are UTF-8 with standard CSV quoting. Case and passage IDs are text; preserve leading zeros. Semicolons delimit ID lists only in the finding map and illustrative-case fields. Multiline excerpt cells are quoted CSV fields. Empty or unestablished values must not be converted into negative observations.

The corpus is 59 interviews. The 20 case summaries are a selected comparison set; the 19 windows cover 10 cases. These are overlapping views of one corpus, not three independent samples.

## 01_corpus_overview.csv

Rows: 28

| Field | Meaning |
|---|---|
| `profile_dimension` | Study descriptor; not a participant-level variable. |
| `reported_value` | Reported descriptor or explicitly stated information limit. |

## 03_corpus_inventory.csv

Rows: 59

| Field | Meaning |
|---|---|
| `case_id` | De-identified archive identifier; read as text and preserve leading zeros. |
| `analytic_status` | Included in the current 59-interview analytic corpus. |
| `working_record_status` | Nature of the retained working record; does not certify independent translation validation. |
| `quotation_status` | Limits on quotation/source verification; does not certify a new listening audit. |
| `contrastive_anchor_status` | yes/no membership in the 20-case contrastive summary set. |
| `source_access` | Access to complete source records; restricted for every case. |

## 04_operational_definitions.csv

Rows: 18

| Field | Meaning |
|---|---|
| `construct` | Construct or reporting rule. |
| `operational_definition` | Definition used in the current article. |
| `analytic_boundary` | What the definition does not establish; preserve distinctions between absence, uncertainty, and inapplicability. |
| `relationship_to_prior_literature` | Conceptual relationship; these rows are not validated measurement scales. |
| `illustrative_case_ids` | Illustrative case identifiers or a conceptual/rule boundary; not a complete coding census. |

## 05_contrastive_case_summaries.csv

Rows: 20

| Field | Meaning |
|---|---|
| `case_id` | Included case identifier; the 20 summaries are a selected comparison set. |
| `narrated_incident_or_contrast` | De-identified account of the incident, practice, or contrast. |
| `descriptive_coding_function` | Descriptive coding function retained in the comparison. |
| `analytic_role` | Role of the case in the current analysis. |
| `boundary_or_caution` | Scope limit; do not interpret summary membership as prevalence. |

## 06_selected_source_windows.csv

Rows: 19

| Field | Meaning |
|---|---|
| `passage_id` | P01-P19 key; joins to the excerpts and finding map. |
| `case_id` | Included case identifier. |
| `working_record_start` | Inclusive turn-start marker in the English working record; HH:MM:SS.mmm. |
| `working_record_end_exclusive` | Exclusive closing marker in the English working record; not an independently verified audio boundary. |
| `reported_action_and_attribution` | Current analytic interpretation of reported action. |
| `evidence_boundary` | Evidence form, uncertainty, and speaker-tag restrictions. |

## 07_selected_evidence_excerpts.csv

Rows: 19

| Field | Meaning |
|---|---|
| `passage_id` | Join key for the source-window ledger. |
| `case_id` | Included case identifier. |
| `article_section_or_role` | Current manuscript section or supplementary analytic role. |
| `selected_english_excerpt` | Selected English working-record turns with original timestamp and opaque speaker tag. Bracketed privacy replacements are explicit; no sentence polishing has been applied. |
| `selection_and_redaction_note` | Selection/non-adjacency and privacy-replacement explanation. |
| `verification_scope` | Text-match verification scope; not original-language/audio certification. |
| `evidence_boundary` | Interpretive limit carried over from the source-window ledger. |

## 08_finding_evidence_map.csv

Rows: 4

| Field | Meaning |
|---|---|
| `article_section` | Section identifier in the current manuscript. |
| `finding` | Bounded interpretive finding. |
| `passage_ids` | Semicolon-separated references to P01-P19; not separate observations. |
| `comparison_case_ids` | Semicolon-separated included case identifiers; preserves within-case comparisons. |
| `inference_limit` | Limits on what the linked evidence establishes. |

## Joins and evidence scope

`03_corpus_inventory.csv.case_id` is the membership authority. Every case ID in the contrastive summaries, source windows, and excerpts belongs to that inventory. `passage_id` joins the source-window ledger and excerpts one to one. The finding map references existing passage IDs; its links are not counts.

Attribution uses learner, another person, tool, shared, or unestablished. Shared requires contributions to the same function. Applicability, requirement, occurrence, and outcome are separate. An action being unnecessary, unmentioned, or described as rare does not establish non-occurrence.

The release contains no complete open-coding census, agreement statistics, sample-wide demographic distribution, participant-level interview calendar, or independently validated original-language transcript. Do not derive such quantities from these selected summaries.
