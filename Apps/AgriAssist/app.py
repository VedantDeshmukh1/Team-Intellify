import streamlit as st
import requests
import json
from PIL import Image
import io
import base64
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage
import os

# Set up OpenAI API (replace with your actual API key)
openai_api_key = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = openai_api_key

st.title("AgriAssist: Your Smart Farming Companion")

# Sidebar for navigation
page = st.sidebar.selectbox("Choose a feature", ["Crop Recommendation", "Disease Identification"])

def get_openai_response(prompt):
    chat = ChatOpenAI(model='gpt-3.5-turbo', api_key = openai_api_key )
    output = chat.invoke([HumanMessage(content=prompt)])
    return output.content

if page == "Crop Recommendation":
    st.header("Crop Recommendation System")

    # Input fields
    country = st.selectbox("Select your country", ["India", "USA"])

    if country == "India":
      soil_type = st.selectbox("Soil Type", ["Alluvial Soil", "Black Soil", "Red Soil", "Laterite Soil", "Desert Soil", "Mountain Soil", "Saline Soil", "Peaty Soil"])
      climate = st.selectbox("Climate", ["Tropical Wet", "Tropical Wet and Dry", "Tropical Semi-arid", "Tropical Arid", "Subtropical Humid", "Mountain Climate"])
      rainfall = st.slider("Average Annual Rainfall (mm)", 300, 3000, 1000)
      temp_range = st.slider("Temperature Range (°C)", 0, 50, (20, 35))

    elif country == "USA":
      soil_type = st.selectbox("Soil Type", ["Mollisols", "Alfisols", "Ultisols", "Aridisols", "Entisols", "Inceptisols", "Vertisols", "Spodosols", "Andisols", "Histosols"])
      climate = st.selectbox("Climate", ["Continental", "Subtropical", "Mediterranean", "Arid", "Semi-arid", "Subarctic", "Tropical"])
      rainfall = st.slider("Average Annual Rainfall (mm)", 0, 2000, 750)
      temp_range = st.slider("Temperature Range (°C)", -20, 45, (10, 30))


    if st.button("Get Crop Recommendations"):
        prompt = f"""
        As an agricultural expert, recommend 5 suitable crops based on the following conditions:
        Soil Type: {soil_type}
        Climate: {climate}
        Average Annual Rainfall: {rainfall} mm
        Temperature Range: {temp_range[0]}°C to {temp_range[1]}°C

        For each crop, provide a brief explanation of why it's suitable.
        """

        with st.spinner("Generating recommendations..."):
            recommendations = get_openai_response(prompt)

        st.subheader("Recommended Crops:")
        st.write(recommendations)

elif page == "Disease Identification":
    st.header("Crop Disease Identification")

    uploaded_file = st.file_uploader("Upload an image of the affected plant", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert image to base64
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

        if st.button("Identify Disease"):
            chat = ChatOpenAI(model='gpt-4-vision-preview', max_tokens=512)

            prompt = """
            As an agricultural expert, analyze the following image of a plant.
            Identify any visible diseases or pests affecting the plant. If a disease is present, provide the following information:
            1. Name of the disease
            2. Symptoms
            3. Possible causes
            4. Recommended treatment or management practices

            If no disease is apparent, state that the plant appears healthy and provide general care tips.
            """

            with st.spinner("Analyzing image..."):
                output = chat.invoke([
                    HumanMessage(
                        content=[
                            {"type": "text", "text": prompt},
                            {"type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}",
                                "detail": "auto"
                                }}
                            ])
                ])

            st.subheader("Disease Analysis:")
            st.write(output.content)

st.sidebar.markdown("---")
st.sidebar.info("This app uses AI to provide crop recommendations and identify plant diseases. Always consult with local agricultural experts for the most accurate advice.")