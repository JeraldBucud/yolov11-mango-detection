"""Run mango detection with the fine-tuned YOLOv11-n checkpoint."""

from __future__ import annotations

import argparse
from pathlib import Path

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect mangoes in an image, video, or directory."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Path to an image, video, directory, webcam index, or supported URL.",
    )
    parser.add_argument(
        "--weights",
        default="models/best.pt",
        help="Path to the trained YOLO checkpoint (default: models/best.pt).",
    )
    parser.add_argument(
        "--output",
        default="runs/predict",
        help="Output directory (default: runs/predict).",
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Confidence threshold between 0 and 1 (default: 0.25).",
    )
    parser.add_argument(
        "--iou",
        type=float,
        default=0.50,
        help="IoU threshold for non-maximum suppression (default: 0.50).",
    )
    parser.add_argument(
        "--imgsz",
        type=int,
        default=640,
        help="Inference image size (default: 640).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    weights = Path(args.weights)
    if not weights.is_file():
        raise FileNotFoundError(
            f"Model checkpoint not found: {weights.resolve()}"
        )

    if not 0.0 <= args.conf <= 1.0:
        raise ValueError("--conf must be between 0 and 1.")

    if not 0.0 <= args.iou <= 1.0:
        raise ValueError("--iou must be between 0 and 1.")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    model = YOLO(str(weights))
    results = model.predict(
        source=args.source,
        imgsz=args.imgsz,
        conf=args.conf,
        iou=args.iou,
        save=True,
        project=str(output.parent),
        name=output.name,
        exist_ok=True,
    )

    saved_dir = getattr(results[0], "save_dir", output) if results else output
    print(f"Prediction complete. Annotated outputs: {saved_dir}")


if __name__ == "__main__":
    main()
