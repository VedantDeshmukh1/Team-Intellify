# Team-Intellify

## 1. MediScan: Medical Document Analyzer
[Mediscan Deployed link](https://mediscan-medical-document-analyzer.streamlit.app/)

### 🏥 Overview
MediScan is an AI-powered Streamlit application designed to help patients better understand medical documents and assess their symptoms. It addresses the common challenge of medical jargon and complex prescriptions by providing simple explanations and preliminary health assessments.

[MediScan_Demo.webm](https://github.com/VedantDeshmukh1/Team-Intellify/assets/97503802/068119e3-1a27-4100-bacc-f747514c6abf)



### 🌟 Features
- **Medical Document Analysis**: Upload and analyze medical documents, prescriptions, or test results.
- **Medication Explanation**: Get simple explanations of medications and dosages.
- **Symptom Checker**: Receive preliminary assessments based on described symptoms.
- **User-Friendly Interface**: Easy-to-use Streamlit app with separate tabs for different functionalities.

### 🛠 Technologies Used
- Python
- Streamlit
- Google Generative AI (Gemini model)
- Pillow (PIL)
- python-dotenv

### 📋 Prerequisites
- Python 3.7+
- A Google API key with access to the Gemini model

### 🚀 Installation and Setup
1. Clone the repository:
   ```
   git clone https://github.com/VedantDeshmukh1/Team-Intellify.git
   cd Apps/MediScan
   ```
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

### 🖥 Usage
1. **Document Analysis**:
   - Navigate to the "Document Analysis" tab.
   - Upload a medical document (supported formats: JPG, JPEG, PNG, PDF).
   - Optionally, enter any specific questions about the document.
   - Click "Analyze Document" to receive an AI-generated explanation.
2. **Symptom Checker**:
   - Switch to the "Symptom Checker" tab.
   - Describe your symptoms in the text area provided.
   - Click "Check Symptoms" for a preliminary assessment.

### ⚠️ Disclaimer
MediScan is designed to assist in understanding medical information and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.

------------



## 2. AgriAssist: Smart Farming Companion  
[AgriAssist Deployed link](https://intellify-agriassist.streamlit.app/)


### 🌱 Overview
AgriAssist is an AI-powered application designed to revolutionize farming practices by providing intelligent crop recommendations, disease identification, and customized crop calendars. It aims to empower Indian farmers with data-driven insights for sustainable and efficient agriculture.


[AgriAssist_Demo.webm](https://github.com/VedantDeshmukh1/Team-Intellify/assets/97503802/739c22d3-6563-411e-953e-288bdd8903e2)


### 🌟 Features
- **Crop Recommendation System**: Tailored suggestions based on soil type, climate, rainfall, and temperature.
- **Disease Identification**: Instant plant disease diagnosis using advanced image recognition.
- **Crop Calendar**: Customized calendars with region-specific agricultural practices.
- **User-Friendly Interface**: Streamlit app with intuitive navigation and clear results presentation.

### 🛠 Technologies Used
- Python
- Streamlit
- OpenAI's GPT-3.5 and GPT-4
- Pillow (PIL)
- Langchain

### 📋 Prerequisites
- Python 3.7+
- An OpenAI API key

### 🚀 Installation and Setup
1. Clone the repository:
   ```
   git clone https://github.com/VedantDeshmukh1/Team-Intellify.git
   cd Apps/AgriAssist
   ```
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key in the `secrets.toml` file:
   ```
   [openai]
   OPENAI_API_KEY = "your_api_key_here"
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

### 🖥 Usage
1. **Crop Recommendation**:
   - Select your state, soil type, climate, and input rainfall and temperature data.
   - Click "Get Crop Recommendations" for AI-generated suggestions.
2. **Disease Identification**:
   - Upload an image of the affected plant.
   - Click "Identify Disease" for analysis and treatment recommendations.
3. **Crop Calendar**:
   - Enter crop name, state, season, and farm size.
   - Click "Generate Crop Calendar" for a customized agricultural timeline.

### ⚠️ Disclaimer
AgriAssist provides general agricultural guidance and should not replace expert advice. Always consult with local agricultural experts for the most accurate and up-to-date information.

## 🤝 Contributing
Contributions to improve both MediScan and AgriAssist are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact
For any queries or suggestions, please open an issue on this GitHub repository.
