import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(image, input_prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    prompt_template = f"""
    As a medical expert, analyze the provided medical document image and address the following:
    1. Provide a concise summary of key findings, diagnosis, or treatment plan.
    2. Explain any medications mentioned, including dosages, in simple terms.
    3. Highlight any important instructions or precautions for the patient.
    4. If applicable, suggest when the patient should seek further medical attention.
    5. Address any specific questions or concerns mentioned in the user's input: {input_prompt}

    Please use plain language for easy understanding by patients.
    """
    
    response = model.generate_content([prompt_template, image])
    return response.text

def symptom_checker(symptoms):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    prompt = f"""
    As a medical professional, provide a preliminary assessment based on the following symptoms: {symptoms}
    Include:
    1. Possible conditions (emphasize these are potential, not definitive diagnoses)
    2. Suggested home care measures, if applicable
    3. Clear advice on when to seek immediate medical attention
    4. Any lifestyle or preventive recommendations

    Emphasize that this is not a substitute for professional medical advice.
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    st.set_page_config(page_title="MediScan: Medical Document Analyzer", page_icon="🏥")
    
    st.title("🏥 MediScan: Medical Document Analyzer")
    st.write("Upload medical documents or describe symptoms for AI-powered analysis and explanation.")

    tab1, tab2 = st.tabs(["Document Analysis", "Symptom Checker"])

    with tab1:
        st.header("📄 Medical Document Analysis")
        input_prompt = st.text_input("Any specific questions about the document?", key="doc_input")
        uploaded_file = st.file_uploader("Upload a medical document", type=["jpg", "jpeg", "png", "pdf"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Document", use_column_width=True)

            if st.button("Analyze Document"):
                with st.spinner("Analyzing document..."):
                    response = get_gemini_response(image, input_prompt)
                st.subheader("Analysis Results:")
                st.write(response)

    with tab2:
        st.header("🩺 Symptom Checker")
        symptoms = st.text_area("Describe your symptoms:")
        if st.button("Check Symptoms"):
            with st.spinner("Analyzing symptoms..."):
                response = symptom_checker(symptoms)
            st.subheader("Preliminary Assessment:")
            st.write(response)

    st.sidebar.title("About MediScan")
    st.sidebar.info(
        "MediScan helps patients understand medical documents and assess symptoms. "
        "Always consult with healthcare professionals for accurate medical advice."
    )

if __name__ == "__main__":
    main()