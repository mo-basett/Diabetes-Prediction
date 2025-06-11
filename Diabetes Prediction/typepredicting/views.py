from django.shortcuts import render

import joblib
import pandas as pd

# Load model & label encoder
model = joblib.load("typepredicting/diabetes_model.pkl")
label_encoder = joblib.load("typepredicting/label_encoder.pkl")

# Define feature names
feature_columns = ["Insulin Levels", "Age", "BMI", "Blood Pressure", "Cholesterol Levels", 
                   "Waist Circumference","Blood Glucose Levels", "Pancreatic Health", "Pulmonary Function", "Neurological Assessments","Digestive Enzyme Levels"]

def predict_diabetes(request):
    if request.method == "POST":
        try:
            # Get input values
            values = [float(request.POST[col]) for col in feature_columns]

            # Create dataframe
            input_df = pd.DataFrame([values], columns=feature_columns)

            # Make prediction
            prediction = model.predict(input_df)
            predicted_class = label_encoder.inverse_transform(prediction)[0]

            return render(request, "typepredicting.html", {"prediction": predicted_class})
        except Exception as e:
            return render(request, "typepredicting.html", {"error": str(e)})

    return render(request, "typepredicting.html")
# Create your views here.
