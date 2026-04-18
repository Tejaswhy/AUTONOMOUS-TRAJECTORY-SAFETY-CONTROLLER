1.
This project implements an AI-powered healthcare assistance system designed for early-stage diagnosis and patient monitoring. It combines computer vision and natural language processing techniques to analyze medical images and symptoms, providing a comprehensive and intelligent health screening solution.



2.
The system is built using Streamlit for the user interface, PyTorch for deep learning models, EfficientNet for image classification, and BioBERT for symptom-based disease prediction. It offers an interactive and user-friendly platform for both patients and healthcare professionals.



3.
The application accepts multiple types of inputs, including eye images, tongue images, skin images, and textual symptom descriptions. By combining these inputs, the system provides a more holistic understanding of the patient’s condition.



4.
The eye analysis module uses a trained image classification model to detect conditions such as cataract, thyroid-related eye signs, uveitis, watery eyes caused by fever, and normal eye health. This enables quick visual screening for common eye-related diseases.



5.
The tongue analysis module evaluates tongue images to identify possible health conditions including oral cancer, diabetes indicators, prediabetes signs, and healthy tongue status. This helps in identifying internal health issues through visual markers.



6.
The skin analysis module allows users to upload skin images and detects various dermatological conditions such as melanoma, benign keratosis, atopic dermatitis, ringworm or candidiasis, squamous cell carcinoma, and vascular lesions.



7.
In addition to image-based analysis, the system includes a symptom-based prediction module powered by BioBERT. Users can input symptoms like fever, fatigue, headache, vomiting, breathing issues, and body pain, and the model predicts the most likely disease.



8.
The system combines predictions from image analysis and symptom analysis to generate a final diagnosis along with a confidence score. This multi-modal approach improves the accuracy and reliability of the results.



9.
A key feature of the project is patient history tracking. Each user is assigned a unique patient ID, and all uploaded images are stored for future reference. The system also compares past and current images using feature embeddings to monitor changes over time.



10.
The application includes a reminder system that allows users to schedule notifications for medication, hydration, sugar checks, and follow-up consultations. Overall, this project demonstrates an integrated healthcare solution that combines AI, data tracking, and user interaction, with future scope for cloud integration, doctor dashboards, and advanced anomaly detection.
