# Model card: YOLOv11-n mango detector

## Model details

- Architecture: YOLOv11-n
- Task: object detection
- Classes: `mango`
- Input size used for training and evaluation: 640 × 640
- Final checkpoint: `best.pt`
- Framework: Ultralytics YOLO
- Selected experiment: tuned experiment
- Optimiser: AdamW
- Initial learning rate: 0.0008
- Planned epochs: 100
- Training stopped: epoch 77
- Best recorded epoch: 57

## Checkpoint access

The checkpoint is not stored directly in this repository. Download it from:

https://drive.google.com/file/d/1foj6L949Kb_rbnAZJTuc2-E9Z3bt7rs3/view

Place it at `models/best.pt` before running inference or checkpoint-dependent evaluation.

## Evaluation data

The final checkpoint was evaluated on a held-out test split containing:

- 86 images
- 694 annotated mango instances

## Final metrics

| Metric | Result |
|---|---:|
| Precision | 0.936436 |
| Recall | 0.971182 |
| mAP@0.5 | 0.989359 |
| mAP@0.5:0.95 | 0.704345 |

## Intended use

This checkpoint is intended for:

- Education and research
- Mango-detection experiments
- Prototype orchard-image analysis
- Further evaluation on additional orchard imagery

## Out-of-scope use

This checkpoint has not been validated for:

- Commercial crop forecasting
- Safety-critical agricultural decisions
- Autonomous harvesting
- Detection of fruit varieties, ripeness, damage or disease

Additional data, evaluation and system-level testing would be required for these uses.

## Limitations

Performance may decrease with orchards, camera systems, cultivars, seasons, lighting conditions, severe occlusion, small mangoes or motion blur that are not represented in the training data.

The reported results come from one held-out test split and do not establish performance across broader field conditions.

## Licensing

The checkpoint was produced using Ultralytics YOLO. The repository is released under AGPL-3.0-only, and the training dataset is attributed separately under CC BY 4.0. See `LICENSE` and `NOTICE.md`.
