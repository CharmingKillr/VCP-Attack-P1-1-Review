# VCP-Attack VQA / SNLI-VE prompt direct review — batch 01

- Review time: 2026-10-20 21:25 Asia/Shanghai
- Reviewer: assistant direct review of task records, prompt text, and the two original images; no separate audit model was used.
- Scope: 2 completed task records out of 2,000. This is an initial case review, not a representative sample and not the 80,000-prompt release gate.
- Gate rule: only exact 20-source + 20-target records can be reviewed; invalid, partial, or uncertain records do not pass.

## VQA: `vqa_val_0057`

- Original image: `/home/nfs_storage/jw_backup/dataset/val2014/COCO_val2014_000000000764.jpg`
- Prompt record: `runs/t2i_reference_bank_80k_v15_20261019/prompt_writer_qwen38_v15_full/shard_01/vqa_val_0057.json`
- Question: “What is around the woman's neck?”
- Source answer: `scarf` (all 10 source annotations say `scarf`)
- Target answer: `tie`
- Count: 20 source / 20 target.
- Image check: the foreground woman visibly wears a scarf around her neck; the source answer is supported.
- Semantic check: source prompts consistently depict a scarf. Target prompts explicitly request a necktie, a plausible same-type alternative, so the intended answer contrast is present.
- Diversity/coherence check: prompts preserve the queried woman/accessory and vary framing, pose, and small details, but cluster heavily around parks/gardens/cherry blossoms and reuse near-identical sentence templates. Several target formulations (“wool necktie wrapped around her neck”, “cozy necktie”, “neck tie fluttering”) could yield scarf-like or ambiguous images.
- Decision: **REVISE — not approved for the image-generation gate yet.** Preserve the task and history; revise/reselect the target prompt bank rather than counting it as passed.

## SNLI-VE: `snli_ve_test_0000`

- Original image: `/home/nfs_storage/jw_backup/dataset/flickr30k-images/1011572216.jpg`
- Prompt record: `runs/t2i_reference_bank_80k_v15_20261019/prompt_writer_qwen38_v15_full/shard_00/snli_ve_test_0000.json`
- Premise: “A beautiful bride walking on a sidewalk with her new husband.”
- Hypothesis: “A couple walks outdoors together.”
- Source label: `entailment`; target label: `contradiction`.
- Count: 20 source / 20 target.
- Image check: the photo shows a bride and groom together outdoors on a sidewalk. The still image alone does not establish motion, but the supplied premise explicitly says they are walking.
- Semantic check: source prompts explicitly depict a couple walking outdoors; target prompts explicitly depict one woman walking alone, which conflicts with “a couple … together.”
- Pair/diversity check: the two banks retain the wedding/outdoor-pavement context and vary background, framing, and lighting. Wording is somewhat templated, but the decisive participant relation is consistent and clear.
- Decision: **PASS for text semantics, with a moderate-diversity/template-reuse note.** This single-task decision does not satisfy or imply the full-bank gate.

## Batch result

- Directly reviewed: 2 tasks / 80 prompts.
- Pass: 1 task; revise: 1 task; uncertain: 0.
- Full prompt gate: **BLOCKED / not evaluated**. No images are authorized by this batch review.
- No generated prompt files were edited or overwritten.
