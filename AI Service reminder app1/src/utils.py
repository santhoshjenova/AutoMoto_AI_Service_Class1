import joblib
import pandas as pd

def load_model(model_path):
    """Load and return a saved joblib model pipeline."""
    return joblib.load(model_path)

def create_input_dataframe(features_dict, columns_order=None):
    """Create a single-row DataFrame from user input dictionary."""
    df = pd.DataFrame([features_dict])
    if columns_order:
        df = df[columns_order]
    return df

def postprocess_prediction(pred, feedback_score, urgency_map=None):
    """Generate reminder message and communication channels based on prediction."""
    urgency = urgency_map[pred] if urgency_map else str(pred)
    if pred == 1:
        if feedback_score <= 2:
            msg = (
                "We noticed your previous feedback and want to ensure a better experience this time. "
                "Your vehicle is due for service soon. Special offer: 15% discount on your next service."
            )
            channels = "Phone, WhatsApp, Email"
            segment = "Critical"
        else:
            msg = "Your vehicle is due for service soon. Please schedule your appointment."
            channels = "WhatsApp, Email, SMS"
            segment = "High/Medium"
    else:
        msg = "No immediate service is due!"
        channels = "Email"
        segment = "Low"
    return urgency, msg, channels, segment
