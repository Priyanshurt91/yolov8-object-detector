"""
Train YOLOv8 using ultralytics API.
Example:
python src/train.py --data data/dataset.yaml --epochs 50 --img 640
"""
import argparse
from ultralytics import YOLO


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--data', required=True, help='path to dataset.yaml (train/val paths, nc, names)')
    p.add_argument('--epochs', type=int, default=50)
    p.add_argument('--img', type=int, default=640)
    p.add_argument('--project', default='runs/train')
    p.add_argument('--name', default='exp')
    p.add_argument('--batch', type=int, default=16)
    return p.parse_args()


def main():
    args = parse_args()
    # start from a pretrained small model
    model = YOLO('yolov8n.pt')
    model.train(data=args.data, epochs=args.epochs, imgsz=args.img, batch=args.batch, project=args.project, name=args.name)


if __name__ == '__main__':
    main()
