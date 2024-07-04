import streamlit as st
import requests
import json
from PIL import Image
import io
import base64
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage
import os
import toml

# Set up OpenAI API (replace with your actual API key) in secrets.toml file
secrets = toml.load("secrets.toml")
openai_api_key = secrets["openai"]["OPENAI_API_KEY"]

st.title("AgriAssist: Your Smart Farming Companion for Indian Agriculture")

# Sidebar for navigation
page = st.sidebar.selectbox("Choose a feature", ["Crop Recommendation", "Disease Identification", "Crop Calendar"])

def get_openai_response(prompt):
    chat = ChatOpenAI(model='gpt-3.5-turbo', api_key=openai_api_key)
    output = chat.invoke([HumanMessage(content=prompt)])
    return output.content

def get_crop_calendar(crop, state, season, farm_size):
    prompt = f"""
    As an agricultural expert specializing in Indian farming, provide a detailed crop calendar for {crop} in {state}, India,
    considering the {season} season and a farm size of {farm_size} acres.
    Include the following information:
    1. Ideal sowing/planting time
    2. Key growth stages and their approximate timing
    3. Fertilization schedule (including organic options)
    4. Irrigation practices
    5. Pest and disease management timing (emphasize integrated pest management)
    6. Harvesting period
    7. Post-harvest handling tips
    8. Any government schemes or subsidies applicable for this crop in India

    Present the information in a structured format, considering the typical climate patterns of {state}.
    Include any specific considerations for the given farm size and sustainable farming practices.
    If there are multiple cropping seasons for this crop in {state}, please specify.
    """
    return get_openai_response(prompt)

if page == "Crop Recommendation":
    st.header("Crop Recommendation System")

    # Input fields for India
    state = st.selectbox("Select your state", ["Maharashtra", "Uttar Pradesh", "Punjab", "Gujarat", "Madhya Pradesh", "Other"])
    soil_type = st.selectbox("Soil Type", ["Alluvial Soil", "Black Soil", "Red Soil", "Laterite Soil", "Desert Soil", "Mountain Soil", "Saline Soil", "Peaty Soil"])
    climate = st.selectbox("Climate", ["Tropical Wet", "Tropical Wet and Dry", "Tropical Semi-arid", "Tropical Arid", "Subtropical Humid", "Mountain Climate"])
    rainfall = st.slider("Average Annual Rainfall (mm)", 300, 3000, 1000)
    temp_range = st.slider("Temperature Range (°C)", 0, 50, (20, 35))

    if st.button("Get Crop Recommendations"):
        prompt = f"""
        As an agricultural expert specializing in Indian farming, recommend 5 suitable crops based on the following conditions:
        State: {state}
        Soil Type: {soil_type}
        Climate: {climate}
        Average Annual Rainfall: {rainfall} mm
        Temperature Range: {temp_range[0]}°C to {temp_range[1]}°C

        For each crop, provide:
        1. A brief explanation of why it's suitable
        2. Basic cultivation tips
        3. Any relevant government schemes or subsidies in India
        """

        with st.spinner("Generating recommendations..."):
            recommendations = get_openai_response(prompt)

        st.subheader("Recommended Crops:")
        st.write(recommendations)

elif page == "Crop Calendar":
    st.header("Crop Calendar for Indian Agriculture")
    
    # Input fields
    crop = st.text_input("Enter the crop name:")
    state = st.selectbox("Select your state", ["Maharashtra", "Uttar Pradesh", "Punjab", "Gujarat", "Madhya Pradesh", "Other"])
    
    # Seasons in India
    season = st.selectbox("Select growing season:", ["Kharif (Monsoon)", "Rabi (Winter)", "Zaid (Summer)"])
    farm_size = st.number_input("Farm size (in acres):", min_value=0.1, value=1.0, step=0.1)
    
    if st.button("Generate Crop Calendar"):
        if crop and state:  # Ensure both crop and state are provided
            with st.spinner("Generating crop calendar..."):
                calendar = get_crop_calendar(crop, state, season, farm_size)
            
            st.subheader(f"Crop Calendar for {crop} in {state}, India:")
            st.write(calendar)
            
            # Add a download button for the calendar
            st.download_button(
                label="Download Crop Calendar",
                data=calendar,
                file_name=f"crop_calendar_{crop}_{state}_{season}.txt",
                mime="text/plain"
            )
        else:
            st.warning("Please enter both crop name and state to generate the calendar.")

    # Tips section
    st.subheader("Tips for Indian Farmers:")
    st.markdown("""
    - This calendar is a general guide. Always consider local conditions and expert advice.
    - Adjust practices based on local weather patterns and soil conditions.
    - Stay updated on government schemes and subsidies for agriculture.
    - Consider water-saving irrigation techniques like drip irrigation.
    - Explore organic farming methods for sustainable agriculture.
    - Regularly check with your local Krishi Vigyan Kendra for region-specific advice.
    """)

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
            As an agricultural expert specializing in Indian crops, analyze the following image of a plant.
            Identify any visible diseases or pests affecting the plant. If a disease is present, provide the following information:
            1. Name of the disease
            2. Symptoms
            3. Possible causes
            4. Recommended treatment or management practices (including organic options)
            5. Preventive measures suitable for Indian farming conditions

            If no disease is apparent, state that the plant appears healthy and provide general care tips relevant to Indian agriculture.
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
st.sidebar.info("This app uses AI to provide crop recommendations and identify plant diseases for Indian agriculture. Always consult with local agricultural experts for the most accurate advice.")