


from django.shortcuts import render
import os
import joblib
import pandas as pd
from django.conf import settings

# Load model
model_path = os.path.join(settings.BASE_DIR, 'diabetes_predictor', 'models', 'earlydiabetes_model.pkl')
model = joblib.load("diabetes_predictor/earlydiabetes_model.pkl")

# Define features expected by the model
feature_columns = ["polyuria", "polydipsia", "sudden_weight_loss", "weakness", "polyphagia", 
                   "genital_thrush", "visual_blurring", "itching", "irritability", 
                   "delayed_healing", "partial_paresis", "muscle_stiffness", "alopecia", "obesity"]

def predict_diabetes(request):
    prediction = None
    error = None

    if request.method == 'POST':
        try:
            input_data = []
            for feature in feature_columns:
                value = int(request.POST.get(feature, 0))
                input_data.append(value)

            user_input_df = pd.DataFrame([input_data], columns=feature_columns)
            result = model.predict(user_input_df)[0]

            if result == 1:
                prediction = "You might be diabetic. Please consult a doctor for confirmation and advice."
            else:
                prediction = "You are likely not diabetic based on symptoms."

        except Exception as e:
            error = f"Error occurred: {e}"

    return render(request, "diabetes_form.html", {"prediction": prediction, "error": error})

