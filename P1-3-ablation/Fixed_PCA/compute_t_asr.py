"""Recompute targeted attack success rates from the experiment records."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TASKS = ("VQA", "VE")
SAMPLES_PER_MODEL = 1_000


def count_successes(path, task):
    sample_ids = set()
    hits = clean_correct_count = 0
    with path.open(encoding="utf-8") as stream:
        for line_no, line in enumerate(stream, start=1):
            row = json.loads(line)
            sample_id = row["sample_id"]
            clean_correct = row["clean_correct"]
            target_hit = row["target_hit"]
            if (
                sample_id in sample_ids
                or row["task"] != task
                or row["victim_model"] != path.stem
                or type(clean_correct) is not bool
                or type(target_hit) is not bool
            ):
                raise ValueError(f"{path}:{line_no} has an inconsistent sample record")
            sample_ids.add(sample_id)
            clean_correct_count += clean_correct
            hits += clean_correct and target_hit
    if len(sample_ids) != SAMPLES_PER_MODEL or clean_correct_count == 0:
        raise ValueError(f"{path} must contain {SAMPLES_PER_MODEL} unique samples and at least one correct clean answer")
    return hits, clean_correct_count


def main():
    print("T-ASR (%) = 100 × count(clean_correct AND target_hit) / count(clean_correct)")
    print("task\tvictim_model\ttarget_hits_among_clean_correct\tclean_correct\tT-ASR (%)")
    for task in TASKS:
        files = sorted((ROOT / "results" / task.lower()).glob("*.jsonl"))
        if len(files) != 4:
            raise ValueError(f"{task} must contain results for 4 victim models")
        for path in files:
            hits, clean_correct = count_successes(path, task)
            percent = 100 * hits / clean_correct
            print(f"{task}\t{path.stem}\t{hits}\t{clean_correct}\t{percent:.2f}")


if __name__ == "__main__":
    main()
