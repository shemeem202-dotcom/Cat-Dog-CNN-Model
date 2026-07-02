import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np

# -------------------------------
# Load Model
# -------------------------------
model = tf.keras.models.load_model("cat_dog_cnn.keras")

# -------------------------------
# Streamlit Page
# -------------------------------
st.set_page_config(
    page_title="Cat vs Dog Classifier",
    page_icon="🐶",
    layout="centered"
)

st.title("🐱 Cat vs Dog Image Classifier")
st.write("Upload an image and the CNN model will predict whether it is a Cat or a Dog.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png", "webp", "avif"]
)

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert("RGB")

    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Resize image
    img = img.resize((128, 128))

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Normalize
    img_array = img_array / 255.0

    prediction = model.predict(img_array)

    probability = float(prediction[0][0])

    st.write(f"Prediction Score: **{probability:.4f}**")

    if probability < 0.5:
        st.success("🐶 Prediction: Dog")
        st.progress(int((1 - probability) * 100))
    else:
        st.success("🐱 Prediction: Cat")
        st.progress(int(probability * 100))