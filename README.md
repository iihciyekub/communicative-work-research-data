# Communicative work research data

This independent data release supports **Who Does the Communicative Work? Learners' Accounts of Supported Chinese-Language Encounters**. It provides the current article's de-identified corpus description, interview guide, operational definitions, contrastive case summaries, and selected evidence chain. Its scope is **59 interviews, 20 contrastive case summaries, and 19 source windows from 10 cases**.

Release version: **1.0.0**. Prepared: **6 October 2026**. Repository: [https://github.com/iihciyekub/communicative-work-research-data](https://github.com/iihciyekub/communicative-work-research-data). This release has no repository DOI assigned. Cite the fixed GitHub release and version rather than a different data deposit.

## What to read

1. [Corpus overview](data/01_corpus_overview.csv) and [59-case inventory](data/03_corpus_inventory.csv) establish the analytic scope.
2. [English interview guide](instruments/02_interview_guide_english.md) documents the elicitation context.
3. [Operational definitions](data/04_operational_definitions.csv) explains how message choice, wording source, delivery or presentation, and trouble-addressing action are distinguished.
4. [20 contrastive case summaries](data/05_contrastive_case_summaries.csv) preserves comparative context.
5. [19 source windows](data/06_selected_source_windows.csv), [readable evidence excerpts](docs/selected_evidence_excerpts.md), and [finding-to-evidence map](data/08_finding_evidence_map.csv) connect the current article's interpretations to selected passages. A [CSV version of the excerpts](data/07_selected_evidence_excerpts.csv) supports machine-readable inspection.
6. [Data dictionary](docs/data_dictionary.md) defines every distributed CSV field. [Methods and access limits](docs/methods_and_access.md) explains what this package can and cannot verify.

## Scope

The study analyses retrospective accounts of Chinese-language encounters and recurring practices within one programme. Its claims concern reported actions and participants' explanations. The selected materials do not estimate configuration prevalence, identify causal acquisition, establish developmental stages, or reconstruct naturally occurring interaction.

The 59 interviews define the corpus. Archive identifiers have gaps and extend to #64; this package contains exactly 59 included cases. The 20 summaries and 19 windows are selected views of that corpus, not additional participants or an exhaustive episode census. Membership is defined by the supplied inventory.

Excerpt wording comes from retained English working records. No language polishing has been applied to these source passages. Bracketed replacements conceal identifying names, places, or national-language cues. Selected passages have been matched to those English records; this does not constitute independent original-language listening, translation-fidelity validation, or certification of speaker identity.

## Confidential material

Raw recordings, complete transcripts, participant names, case-to-country links, consent forms, the case identity key, and identifying governance documents are excluded. They remain restricted because combinations of professional, national, institutional, and life-event information could identify people. This release does not grant access to those materials.

## Integrity and citation

Run `python3 scripts/verify_package.py` using Python 3 and its standard library. The check verifies the SHA-256 manifest, corpus membership, one-to-one passage links, record counts, finding references, and selected disclosure restrictions. It checks the distributed materials, not the accuracy of original recordings or every analytic decision.

Use the repository's **Cite this repository** interface or [CITATION.cff](CITATION.cff). Data and documentation are shared under [CC BY 4.0](LICENSE.md). The validation utility is shared under the MIT licence stated in its header.
