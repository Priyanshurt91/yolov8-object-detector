Dataset structure and quick guide

We use YOLO format (one .txt per image with normalized bbox: class x_center y_center width height).

Structure:

```
data/
  images/
    train/
    val/
  labels/
    train/
    val/
  classes.txt
  dataset.yaml
```

Example `dataset.yaml`:

```yaml
path: data
train: images/train
val: images/val
nc: 1
names: ['object']
```

Annotation workflow (LabelImg -> convert):
1. Use LabelImg to annotate images (save as Pascal VOC xml).
2. Create a `classes.txt` with one class per line.
3. Run:
   ```bash
   python src/utils/labelimg_to_yolo.py --xml_dir data/images/train --classes data/classes.txt
   python src/utils/labelimg_to_yolo.py --xml_dir data/images/val --classes data/classes.txt
   ```
4. Verify `.txt` files appear next to images in `data/images/*` and then move them into `data/labels/*` following the structure above.
