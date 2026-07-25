# Dataset setup

The full dataset is not committed to this repository.

## Source and licence

- Dataset: `mango detection`
- Source: https://universe.roboflow.com/weed-mapping/mango-detection-glzls
- Provider: Roboflow Universe user dataset
- Licence: CC BY 4.0
- Class: `mango`

## Recorded split

| Split | Images |
|---|---:|
| Training | 1,384 |
| Validation | 260 |
| Test | 86 |
| Total | 1,730 |

## Expected local structure

Download the YOLO-format dataset and arrange it as:

```text
data/
└── mangoyolo/
    ├── train/
    │   ├── images/
    │   └── labels/
    ├── valid/
    │   ├── images/
    │   └── labels/
    ├── test/
    │   ├── images/
    │   └── labels/
    └── data.yaml
```

The `data/mangoyolo/` folder is ignored by Git to avoid committing the complete dataset.
The cleaned notebook can also use another location through the `MANGO_DATASET_DIR`
environment variable.

## Sample files

The `samples/` directory contains a small selection of dataset images and matching YOLO
label files for documentation. The original Roboflow filenames are preserved.
