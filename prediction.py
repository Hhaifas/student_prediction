import joblib

model = joblib.load("model/gboost_model.joblib")

def prediction(data):
    result = model.predict(data)
    label = "Graduate" if result[0] == 1 else "Dropout"
    return label