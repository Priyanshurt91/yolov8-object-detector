"""
Convert Pascal VOC XML (LabelImg) to YOLO txt labels.
Saves .txt files alongside images.
"""
import os
import glob
import xml.etree.ElementTree as ET


def convert(xml_file, img_w, img_h, classes):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    out_lines = []
    for obj in root.findall('object'):
        name = obj.find('name').text
        if name not in classes:
            continue
        cls_id = classes.index(name)
        bnd = obj.find('bndbox')
        xmin = float(bnd.find('xmin').text)
        ymin = float(bnd.find('ymin').text)
        xmax = float(bnd.find('xmax').text)
        ymax = float(bnd.find('ymax').text)
        x_center = (xmin + xmax) / 2.0 / img_w
        y_center = (ymin + ymax) / 2.0 / img_h
        w = (xmax - xmin) / img_w
        h = (ymax - ymin) / img_h
        out_lines.append(f"{cls_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")
    return out_lines


def main():
    import argparse
    from PIL import Image
    p = argparse.ArgumentParser()
    p.add_argument('--xml_dir', required=True)
    p.add_argument('--classes', required=True, help='path to classes.txt (one class per line)')
    args = p.parse_args()
    with open(args.classes) as f:
        classes = [x.strip() for x in f.read().splitlines() if x.strip()]
    xml_files = glob.glob(os.path.join(args.xml_dir, '*.xml'))
    for xf in xml_files:
        tree = ET.parse(xf)
        root = tree.getroot()
        img_filename = root.find('filename').text
        img_path = os.path.join(os.path.dirname(xf), img_filename)
        if not os.path.exists(img_path):
            # try jpg
            base = os.path.splitext(xf)[0]
            for ext in ('.jpg', '.jpeg', '.png'):
                candidate = base + ext
                if os.path.exists(candidate):
                    img_path = candidate
                    break
        if not os.path.exists(img_path):
            print('Image not found for', xf)
            continue
        w, h = Image.open(img_path).size
        out = convert(xf, w, h, classes)
        if out:
            txt_path = os.path.splitext(img_path)[0] + '.txt'
            with open(txt_path, 'w') as f:
                f.writelines(out)


if __name__ == '__main__':
    main()
