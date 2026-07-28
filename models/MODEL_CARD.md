# Model card: YOLOv11-n mango detector

## Model details

- Architecture: YOLOv11-n
- Task: object detection
- Classes: `mango`
- Input size used for training/evaluation: 640 × 640
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

Place it at `models/best.pt` before running inference or evaluation.

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

This model is intended for:

- Education and research
- Mango-detection experiments
- Prototype orchard-image analysis
- Evaluation of image-level mango detection and counting workflows

## Out-of-scope use

This model should not be treated as a validated production system for:

- Commercial crop forecasting
- Safety-critical agricultural decisions
- Autonomous harvesting without additional testing
- Detection of fruit varieties, ripeness, damage or disease

## Limitations

Performance may decrease with new orchards, camera systems, cultivars, daytime imagery,
severe occlusion, small mangoes, motion blur or lighting conditions not represented in
the training dataset. The model has not yet been benchmarked on a defined target device
or validated against an independently collected external orchard dataset.

## Licensing

The checkpoint was produced using Ultralytics YOLO. The repository is released under
AGPL-3.0-only, and the training dataset is attributed separately under CC BY 4.0.
See `LICENSE` and `NOTICE.md`.
