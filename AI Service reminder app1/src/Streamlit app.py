import streamlit as st
from utils import load_model, create_input_dataframe, postprocess_prediction

model = load_model("Class_service_reminder_model5.pkl")

# Collect user input as a dictionary: features_dict = {...}

input_df = create_input_dataframe(features_dict)

if st.button("Predict & Generate Reminder"):
    pred = model.predict(input_df)[0]
    urgency, msg, channels, segment = postprocess_prediction(pred, features_dict['feedback_score'], {1:"Urgent", 0:"Not Urgent"})
    st.write(f"Prediction: {urgency}")
    st.markdown(msg)
    st.info(f"Channels: {channels} | Segment: {segment}")
