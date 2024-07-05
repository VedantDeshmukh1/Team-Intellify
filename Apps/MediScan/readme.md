# MediScan: Medical Document Analyzer

## 🏥 Overview

MediScan is an AI-powered Streamlit application designed to help patients better understand medical documents and assess their symptoms. It addresses the common challenge of medical jargon and complex prescriptions by providing simple explanations and preliminary health assessments.

![MediScan Screenshot](https://via.placeholder.com/800x400.png?text=MediScan+Screenshot)

## 🌟 Features

- **Medical Document Analysis**: Upload and analyze medical documents, prescriptions, or test results.
- **Medication Explanation**: Get simple explanations of medications and dosages.
- **Symptom Checker**: Receive preliminary assessments based on described symptoms.
- **User-Friendly Interface**: Easy-to-use Streamlit app with separate tabs for different functionalities.

## 🛠 Technologies Used

- Python
- Streamlit
- Google Generative AI (Gemini model)
- Pillow (PIL)
- python-dotenv

## 📋 Prerequisites

- Python 3.7+
- A Google API key with access to the Gemini model

## 🚀 Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/mediscan.git
   cd mediscan
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

## 🖥 Usage

1. **Document Analysis**:
   - Navigate to the "Document Analysis" tab.
   - Upload a medical document (supported formats: JPG, JPEG, PNG, PDF).
   - Optionally, enter any specific questions about the document.
   - Click "Analyze Document" to receive an AI-generated explanation.

2. **Symptom Checker**:
   - Switch to the "Symptom Checker" tab.
   - Describe your symptoms in the text area provided.
   - Click "Check Symptoms" for a preliminary assessment.

## ⚠️ Disclaimer

MediScan is designed to assist in understanding medical information and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.

## 🤝 Contributing

Contributions to improve MediScan are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any queries or suggestions, please open an issue on this GitHub repository.

---

Made with ❤️ by Intellify
