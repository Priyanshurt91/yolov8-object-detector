import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image

st.set_page_config(page_title='YOLOv8 Object Detection', layout='wide')
st.title('YOLOv8 Object Detection Demo')

weights = st.text_input('Path to weights', 'runs/train/exp/weights/best.pt')
model = None
if st.button('Load model'):
    try:
        model = YOLO(weights)
        st.success('Model loaded')
    except Exception as e:
        st.error(f'Failed to load model: {e}')

uploaded = st.file_uploader('Upload an image', type=['jpg','jpeg','png'])
if uploaded:
    img = Image.open(uploaded).convert('RGB')
    st.image(img, caption='Input', use_column_width=True)
    if model:
        results = model(np.array(img))
        annotated = results[0].plot()
        st.image(annotated, caption='Detection', use_column_width=True)

st.markdown('Run locally with `streamlit run app/app.py`. For Spaces deployment, push this repo to a Hugging Face Space and set it to use Streamlit.')
