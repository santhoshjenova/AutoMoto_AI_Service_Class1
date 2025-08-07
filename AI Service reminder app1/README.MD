
# AI-Based Automobile Service Reminder App

## Project Overview

This project is an AI-driven automobile service reminder system designed for dealerships and service centers. It leverages machine learning and natural language processing models to predict the urgency of vehicle servicing for customers based on vehicle data, customer feedback, and other factors. The system generates personalized reminder messages and suggests suitable communication channels such as WhatsApp, Email, SMS, or Phone calls.

The app is built using:

- A machine learning model trained with vehicle and customer data (saved as a `.pkl` pipeline).
- A Streamlit frontend for user interaction and service reminder visualization.
- Utility functions for clean integration and modular code.
- Support for multiple customer segments and personalized recommendations.

---

## Features

- Predicts whether vehicle service is needed soon or not.
- Generates personalized reminder messages based on AI predictions and customer feedback.
- Suggests preferred communication channels for contacting customers.
- Simple, interactive web UI powered by Streamlit.
- Modular and extensible code base with separate utility functions.
- Ready for deployment on platforms like Streamlit Cloud or any cloud provider.

---

## Folder Structure

```
auto-service-reminder-app/
│
├── models/
│   └── Class_service_reminder_model1.pkl    # Trained ML model pipeline
│
├── data/
│   └── ai_based_service_reminder.csv        # Sample dataset for training/testing
│
├── src/
│   ├── classification.app.py                 # Main Streamlit app
│   ├── utils.py                             # Helper functions for model loading, data prep
│   ├── Streamlit-app.py                     # Simplified Streamlit app version
│
├── requirements.txt                         # Python dependencies
├── README.md                               # This documentation file
```

---

## Installation and Setup

1. **Clone the repository** (or download files):

    ```
    git clone https://github.com/yourusername/auto-service-reminder-app.git
    cd auto-service-reminder-app
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```
    python3 -m venv venv
    source venv/bin/activate   # Linux/macOS
    # or
    venv\Scripts\activate      # Windows
    ```

3. **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

4. **Place your trained model file** (`Class_service_reminder_model1.pkl`) inside the `models/` folder.

5. **Run the Streamlit app:**

    ```
    streamlit run src/classification.app.py
    ```

6. **Use the UI to input vehicle and customer details to generate service reminders.**

---

## Usage

- Fill in vehicle age, odometer reading, last service details, feedback score, and other inputs on the app.
- Click on **Predict & Generate Reminder**.
- View the predicted service urgency, personalized reminder message, and recommended communication channels.
- Use this information to contact customers proactively for vehicle servicing.

---

## Next Steps and Enhancements

- Develop a RESTful API backend using FastAPI or Flask to serve the ML model for mobile/web frontends.
- Integrate push notifications, email, SMS services for automated reminders.
- Extend the model with more features and retrain periodically using new data.
- Add user authentication and vehicle profile management for multi-user support.
- Deploy on cloud platforms like AWS, Google Cloud, or Streamlit Cloud for broader access.

---

## References

- Streamlit documentation: https://docs.streamlit.io/
- Scikit-learn for ML pipeline: https://scikit-learn.org/
- LightGBM for gradient boosting: https://lightgbm.readthedocs.io/

---

## Contact

For questions, suggestions, or collaboration, please contact:

- Your Name or Team Name  
- Email: your.email@example.com  
- GitHub: https://github.com/santhoshjecob97

---

*This project is designed to enhance customer engagement and service efficiency using AI-driven insights for the automobile service industry.*
```