"""
Minimal converter from COCO json annotations to YOLO txt files.
"""
import json
import os
from PIL import Image


def coco_to_yolo(coco_json_path, images_dir, output_dir, classes=None):
    os.makedirs(output_dir, exist_ok=True)
    with open(coco_json_path) as f:
        coco = json.load(f)
    anns = coco['annotations']
    imgs = {im['id']: im for im in coco['images']}
    cat_map = {c['id']: c['name'] for c in coco.get('categories', [])}
    if classes:
        with open(classes) as f:
            class_list = [x.strip() for x in f.readlines() if x.strip()]
    else:
        class_list = sorted(list({c['name'] for c in coco.get('categories', [])}))
    img_ann = {}
    for a in anns:
        img_ann.setdefault(a['image_id'], []).append(a)
    for img_id, ann_list in img_ann.items():
        img = imgs[img_id]
        file_name = img['file_name']
        path = os.path.join(images_dir, file_name)
        if not os.path.exists(path):
            print('Image not found:', path)
            continue
        w, h = Image.open(path).size
        out_lines = []
        for a in ann_list:
            cat_name = cat_map[a['category_id']]
            if cat_name not in class_list:
                continue
            cls_id = class_list.index(cat_name)
            bbox = a['bbox']  # [x,y,width,height]
            x, y, bw, bh = bbox
            x_center = (x + bw/2.0) / w
            y_center = (y + bh/2.0) / h
            w_rel = bw / w
            h_rel = bh / h
            out_lines.append(f"{cls_id} {x_center:.6f} {y_center:.6f} {w_rel:.6f} {h_rel:.6f}\n")
        if out_lines:
            txt_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + '.txt')
            with open(txt_path, 'w') as f:
                f.writelines(out_lines)


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--coco', required=True)
    p.add_argument('--images', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--classes', help='optional classes.txt')
    args = p.parse_args()
    coco_to_yolo(args.coco, args.images, args.out, args.classes)
