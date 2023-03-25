import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter.")

upload_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if upload_image:
    img = Image.open(upload_image)
    gray_img = img.convert("L")
    st.image(gray_img)

if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)


