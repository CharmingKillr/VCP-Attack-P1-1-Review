# VCP prompt audit addendum — duplicate-review reconciliation

- Date: 2026-10-21 (Asia/Shanghai)
- Purpose: reconcile IDs fetched again while switching to authoritative report-based de-duplication. Earlier batch files are preserved unchanged; this addendum is authoritative for the updates below.
- No generator output was modified and no image generation was started.

## Duplicate IDs and disposition

- `snli_ve_test_0000`: already reviewed in batch 73 as PASS. The fresh inspection confirms the earlier PASS; do not count it again.
- `snli_ve_test_0004`: already reviewed in batch 73 as PASS. The fresh line-by-line inspection found target prompt 9 (“Course Closed”) directly conflicts with entering a contest, and prompt 12’s finish-line cue is inconsistent with “about to enter.” Reclassify PASS → REVISE; replace only these outlier prompts in a later version. Do not count the sample again.
- `snli_ve_test_0012`: already reviewed in batch 72 as PASS. The fresh inspection confirms the earlier PASS; do not count it again.
- `snli_ve_test_0016`: already reviewed in batch 72 as REVISE. Reclassify REVISE → INVALID_TASK: the hypothesis asserts a reunion and the parents’ death at the bridge, neither visually observable or responsibly expressible by generated imagery. Replace/reselect the task rather than inventing narrative evidence. Do not count it again.

## Unique complete-bank tally after reconciliation

Batch 336 added one previously unseen complete bank (`snli_ve_test_0808`, REVISE). The four IDs in batches 337–338 were duplicates and add **zero** to the number reviewed. Apply the two reclassifications above to the previous cumulative tally:

- Complete 20+20 banks directly reviewed: **1,401 / 1,502**.
- PASS: **951**.
- REVISE: **447**.
- INVALID_TASK: **3**.
- Complete banks remaining: **101**.
- Arithmetic check: 951 + 447 + 3 = 1,401.

Partial/empty banks and the still-unfilled prompt slots remain outside this complete-bank tally. The earlier batch 337/338 reports are retained as raw review notes; this addendum corrects their duplicate-counting and supersedes the affected classifications.
