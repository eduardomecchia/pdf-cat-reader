import streamlit as st
import pymupdf as pymupdf
from PIL import Image
import io
import torch
import torchvision.transforms as transforms
from torchvision import models
import nltk
from nltk.corpus import stopwords

st.set_page_config(
    page_title="PDF Cat Reader",
    page_icon="😽",
)

st.title('Hi! Welcome to the PDF Cat Reader.')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=False)

def load_model():
    model = models.resnet18(pretrained=True)
    model.eval()
    return model

def transform_image(image_bytes):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0)

def get_prediction(image_bytes, model):
    tensor = transform_image(image_bytes)
    outputs = model(tensor)
    _, predicted = torch.max(outputs.data, 1)
    return predicted.item()

model = load_model()

nltk.download('stopwords')
stop_words = stopwords.words('english')

if uploaded_file is not None:
    doc = pymupdf.open(stream=uploaded_file.read(), filetype="pdf")

    words_count = 0
    images = []

    for page in doc:
        words = page.get_text().lower().split()
        words_count += len([word for word in words if word not in stop_words])

        images += page.get_images()

    st.write(f"Total words in the PDF (excluding stop words): {words_count}")

    cat_class_indices = range(281, 286)  

    if images:
        for idx, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            prediction = get_prediction(image_bytes, model)
            label = 'a cat' if prediction in cat_class_indices else 'something that\'s not a cat'  # The numbers are the class indexes for various cat races in ImageNet

            st.write(f"Image {idx + 1} contains {label}.")
            
    