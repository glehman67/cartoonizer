import cv2
import numpy as np
import streamlit as st
from lib.cartoonizer import Cartoonizer

st.set_page_config(layout="centered", page_icon="favicon.ico", page_title="Griff's Cartoonizer")
st.header("Convert any image to a cartoon!")

uploaded_file = st.file_uploader("Choose a image file", type="jpg")

d = st.slider("Set the diameter of each pixel neighborhood:", 0, 10, 9)
sigmaColor = st.slider("Filter sigma in the color space:", 0, 255, 9)
sigmaSpace = st.slider("Filter sigma in the coordinate space:", 0, 255, 9)
blur_ksize = st.slider("Size of the blurring kernel:", 2, 255, 3)
blur_ksize = blur_ksize if blur_ksize % 2 == 1 else blur_ksize + 1
blockSize = st.slider("Size of a pixel neighborhood that is used to calculate a threshold value for the pixel:", 2, 109, 9)
blockSize = blockSize if blockSize % 2 == 1 else blockSize + 1
constant = st.slider("Constant subtracted from the mean or weighted mean:", 0, 255, 20)
numDownSamples = st.slider("Number of downscaling steps:", 0, 10, 2)
numBilateralFilters = st.slider("Number of bilateral filtering steps:", 0, 50, 15)

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    tmp_canvas = Cartoonizer()
    res = tmp_canvas.render(file_bytes, d=d, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace, blur_ksize=blur_ksize, blockSize=blockSize, C=constant, numBilateralFilters=numBilateralFilters, numDownSamples=numDownSamples)

    # Now do something with the image! For example, let's display it:
    st.image(res, channels="BGR")