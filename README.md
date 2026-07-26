# YOLOv11 Mango Detection

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv11-111F68.svg)](https://docs.ultralytics.com/)
[![License](https://img.shields.io/badge/License-AGPL--3.0-green.svg)](LICENSE)

A computer-vision portfolio project that fine-tunes **YOLOv11-n** to detect mangoes in orchard images. The repository includes a cleaned training notebook, the selected model checkpoint, evaluation metrics, training graphs, sample predictions, dataset attribution, and a reusable inference script.

<p align="center">
  <img src="results/predictions/prediction_01.jpg" alt="YOLOv11-n mango detections" width="620">
</p>

## Project highlights

- Single-class object detection: `mango`
- Fine-tuned YOLOv11-n using pretrained weights
- Baseline and tuned experiments
- Validation-based model selection
- Final evaluation on a held-out test set
- Reusable command-line inference script
- Dataset and model licensing documented

## Final test results

| Metric | Result |
|---|---:|
| Precision | 0.936436 |
| Recall | 0.971182 |
| mAP@0.5 | 0.989359 |
| mAP@0.5:0.95 | 0.704345 |
| Test images | 86 |
| Test instances | 694 |

The tuned model was selected using validation performance before the test set was evaluated.

## Experiment comparison

| Experiment | Purpose | Epochs | Learning rate | mAP@0.5 | mAP@0.5:0.95 | Precision | Recall |
|---|---|---:|---:|---:|---:|---:|---:|
| Experiment 1 | Baseline | 50 | 0.0010 | 0.988831 | 0.701359 | 0.962133 | 0.951333 |
| Experiment 2 | Tuned | 100 planned; stopped at 77 | 0.0008 | 0.990000 | 0.703000 | 0.966000 | 0.956000 |

Experiment 2 reached its best recorded epoch at epoch 57 and was selected as the final model.

## Dataset

The project uses a single-class mango detection dataset with YOLO bounding-box annotations.

| Split | Images |
|---|---:|
| Training | 1,384 |
| Validation | 260 |
| Test | 86 |
| **Total** | **1,730** |

Dataset source:

- Roboflow Universe: `weed-mapping/mango-detection-glzls`
- Licence: **CC BY 4.0**
- Source page: https://universe.roboflow.com/weed-mapping/mango-detection-glzls

The complete dataset is intentionally not committed to this repository. See [`data/README.md`](data/README.md) for setup and attribution instructions.

## Repository structure

```text
yolov11-mango-detection/
├── README.md
├── LICENSE
├── NOTICE.md
├── CITATION.cff
├── requirements.txt
├── config/
│   └── data.yaml
├── data/
│   ├── README.md
│   └── samples/
├── docs/
│   └── README.md
├── models/
│   ├── best.pt
│   └── MODEL_CARD.md
├── notebooks/
│   └── yolov11_mango_detection.ipynb
├── results/
│   ├── graphs/
│   ├── metrics/
│   └── predictions/
└── src/
    └── predict.py
```

## Open in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JeraldBucud/yolov11-mango-detection/blob/main/notebooks/yolov11_mango_detection.ipynb)

The dataset is not stored in the repository. Update `MANGO_DATASET_DIR` in the notebook or set it as an environment variable before running dataset-dependent cells.

## Local installation

```bash
git clone https://github.com/JeraldBucud/yolov11-mango-detection.git
cd yolov11-mango-detection

python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run inference

Predict on one image:

```bash
python src/predict.py --source path/to/mango_image.jpg
```

Predict on a folder:

```bash
python src/predict.py --source path/to/images --conf 0.25
```

By default, the script uses `models/best.pt` and saves annotated outputs under `runs/predict/`.

## Training configuration

| Setting | Value |
|---|---|
| Model | YOLOv11-n |
| Input size | 640 × 640 |
| Batch size | 16 |
| Optimiser | AdamW |
| Initial learning rate | 0.0008 |
| Planned epochs | 100 |
| Early stopping | Stopped at epoch 77 |
| Best recorded epoch | 57 |
| Class | mango |

The recorded training environment used Ultralytics 8.4.52, Python 3.12.13, PyTorch 2.10.0 with CUDA, and a Tesla T4 GPU. Hardware and package differences can change runtime and results.

## Results

### Training history

![Training history](results/graphs/results.png)

### Confusion matrix

![Confusion matrix](results/graphs/confusion_matrix.png)

### Precision-recall curve

![Precision-recall curve](results/graphs/precision_recall_curve.png)

### Prediction examples

| Example 1 | Example 2 | Example 3 |
|---|---|---|
| ![](results/predictions/prediction_01.jpg) | ![](results/predictions/prediction_02.jpg) | ![](results/predictions/prediction_03.jpg) |

## Limitations

- The dataset represents a limited set of orchards and capture conditions.
- Occluded, clustered, small, and poorly illuminated mangoes remain challenging.
- The model detects only one class and does not assess ripeness, variety, disease, or fruit quality.
- Results were measured on one held-out test split and should not be treated as proof of production readiness.
- Inference speed depends on hardware, software versions, image size, and deployment settings.

## Future improvements

- Test images from additional orchards, cultivars, seasons, and lighting conditions.
- Compare YOLOv11-n with larger YOLOv11 variants.
- Add mango counting and fruit-load estimation.
- Add ripeness, damage, or disease classes.
- Deploy an image-upload demonstration with FastAPI or Django.
- Benchmark on local GPUs and edge devices.

## References

- Koirala, A., Walsh, K. B., Wang, Z., & McCarthy, C. (2019). *Deep learning for real-time fruit detection and orchard fruit load estimation: Benchmarking of MangoYOLO*. Precision Agriculture, 20, 1107-1135. https://doi.org/10.1007/s11119-019-09642-0
- Redmon, J., Divvala, S., Girshick, R., & Farhadi, A. (2016). *You Only Look Once: Unified, Real-Time Object Detection*. CVPR.
- Ultralytics. *Ultralytics YOLO documentation*. https://docs.ultralytics.com/

## Author

**Jerald Christopher Bucud**

This project began as academic computer-vision work and was reorganised as a public portfolio repository. Personal student information and assessment-only material have been removed.
