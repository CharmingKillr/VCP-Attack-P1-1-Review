# w_o_L_margin

| 路径 | 内容 |
| --- | --- |
| `results/vqa/<模型>.jsonl` | VQA 逐样本评测结果，每个模型 1,000 条 |
| `results/ve/<模型>.jsonl` | VE 逐样本评测结果，每个模型 1,000 条 |
| `adversarial_images/vqa/<sample_id>.png` | VQA 对抗图 |
| `adversarial_images/ve/<sample_id>.png` | VE 对抗图 |
| `compute_t_asr.py` | 从逐样本评测记录计算各模型的 T-ASR |

模型文件名为 `internvl14`、`ovis16`、`qwen7` 和 `gemma12`。
每行 JSONL 对应一个样本。PNG 文件名与 `sample_id` 一一对应。
