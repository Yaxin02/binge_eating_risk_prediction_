import json
import joblib
import pandas as pd
import os

# Load model relative to this file
MODEL_PATH = os.path.join(os.path.dirname(__file__), "binge_eating_model.joblib")
model = joblib.load(MODEL_PATH)

FEATURE_COLUMNS = [
    "Age", "Gender(0,1)", "BMI", "Weight(kg)", "Waist(cm)",
    "Eduction(0,1,2)", "Alcohol", "T2D", "Sleep apnea syndrome",
    "Gastroesophageal reflux disease", "EDE-Q score (Per-operation)"
]

def main(context):
    """
    Appwrite OpenRuntimes V4 entrypoint
    """
    if context.req.method == 'GET':
        return context.res.json({"message": "Appwrite Binge Eating ML Model is running. Use POST."})
    
    if context.req.method == 'POST':
        try:
            bodyRaw = getattr(context.req, 'bodyRaw', getattr(context.req, 'body_raw', getattr(context.req, 'bodyString', getattr(context.req, 'body_string', None))))
            
            if isinstance(context.req.body, str):
                body = json.loads(context.req.body)
            elif isinstance(context.req.body, dict):
                body = context.req.body
            elif bodyRaw:
                body = json.loads(bodyRaw)
            else:
                body = context.req.bodyJson

            row = pd.DataFrame([[
                float(body.get('age', 0)),
                int(body.get('gender', 0)),
                float(body.get('bmi', 0)),
                float(body.get('weight_kg', 0)),
                float(body.get('waist_cm', 0)),
                int(body.get('education', 0)),
                int(body.get('alcohol', 0)),
                int(body.get('t2d', 0)),
                int(body.get('sleep_apnea_syndrome', 0)),
                int(body.get('gastroesophageal_reflux_disease', 0)),
                float(body.get('ede_q_per_operation', 0)),
            ]], columns=FEATURE_COLUMNS)
            
            prediction = int(model.predict(row)[0])
            probability = float(model.predict_proba(row)[0][1])
            
            return context.res.json({
                "prediction": prediction,
                "probability": probability,
                "saved": False
            })
            
        except Exception as e:
            context.error(f"Error making prediction: {str(e)}")
            return context.res.json({"error": str(e)}, 500)

    return context.res.json({"error": "Method not allowed"}, 405)
