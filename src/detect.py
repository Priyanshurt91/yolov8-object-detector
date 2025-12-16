"""
Detect script using a trained YOLOv8 model.
Example:
python src/detect.py --weights runs/train/exp/weights/best.pt --source 0
"""
import argparse
from ultralytics import YOLO


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--weights', required=True)
    p.add_argument('--source', default='0', help='image, dir, or camera index (0)')
    p.add_argument('--conf', type=float, default=0.25)
    p.add_argument('--save', action='store_true', help='save results to runs/detect')
    return p.parse_args()


def main():
    args = parse_args()
    model = YOLO(args.weights)
    results = model(args.source, conf=args.conf, show=True)
    if args.save:
        for r in results:
            r.save()


if __name__ == '__main__':
    main()
