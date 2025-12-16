# yolov8-object-detector
YOLOv8-based object detection project with Streamlit demo and deployment
# YOLOv8 Object Detector

A complete object-detection project using Ultralytics YOLOv8 with a Streamlit demo and Hugging Face Spaces deployment instructions. Includes training and inference scripts, dataset helpers, and a Dockerfile.

Quickstart

1. Clone the repo:
   ```bash
   git clone https://github.com/Priyanshurt91/yolov8-object-detector.git
   cd yolov8-object-detector
   ```
2. Create a Python environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Prepare your dataset following `data/README.md` (use LabelImg to annotate and convert to YOLO format).
4. Train (example, with GPU):
   ```bash
   python src/train.py --data data/dataset.yaml --epochs 50 --img 640 --batch 16
   ```
5. Run detection on an image or webcam:
   ```bash
   python src/detect.py --weights runs/train/exp/weights/best.pt --source 0
   ```
6. Run the demo locally:
   ```bash
   streamlit run app/app.py
   ```

Hugging Face Spaces Deployment
- Create a new Space (Streamlit) on Hugging Face under your account, link it to this GitHub repository, and set hardware (CPU/GPU) as needed. Spaces will automatically build using `requirements.txt` and run the Streamlit `app/app.py`.

License: MIT
