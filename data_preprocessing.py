import joblib
import numpy as np
import pandas as pd

gboost_model = joblib.load("model/gboost_model.joblib")
scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Application_order = joblib.load("model/scaler_Application_order.joblib")
scaler_Age_at_enrollment = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_1st_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_without_evaluations.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")
scaler_GDP = joblib.load("model/scaler_GDP.joblib")
scaler_Inflation_rate = joblib.load("model/scaler_Inflation_rate.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
scaler_Unemployment_rate = joblib.load("model/scaler_Unemployment_rate.joblib")


# Proses data processing

def data_preprocessing(data):
    data = data.copy()
    df = pd.DataFrame(index=data.index)
    
    
    df['Marital_status']= data['Marital_status'],
    df['Application_mode']= data['Application_mode'],
    df['Application_order'] = scaler_Application_order.transform(np.asarray(data['Application_order']).reshape(-1, 1))
    df['Course']= data['Course'],
    df['Daytime_evening_attendance']= data['Daytime_evening_attendance'],
    df['Previous_qualification']= data['Previous_qualification'],
    df['Previous_qualification_grade'] = scaler_Previous_qualification_grade.transform(np.asarray(data['Previous_qualification_grade']).reshape(-1, 1))
    df['Nacionality']= data['Nacionality'],
    df['Mothers_qualification']= data['Mothers_qualification'],
    df['Fathers_qualification']= data['Fathers_qualification'],
    df['Mothers_occupation']= data['Mothers_occupation'],
    df['Fathers_occupation']= data['Fathers_occupation'],
    df['Admission_grade'] = scaler_Admission_grade.transform(np.asarray(data['Admission_grade']).reshape(-1, 1))
    df['Displaced']= data['Displaced'],
    df['Educational_special_needs']= data['Educational_special_needs'],
    df['Debtor']= data['Debtor'],
    df['Tuition_fees_up_to_date']= data['Tuition_fees_up_to_date'],
    df['Gender']= data['Gender'],
    df['Scholarship_holder']= data['Scholarship_holder'],
    df['Age_at_enrollment'] = scaler_Age_at_enrollment.transform(np.asarray(data['Age_at_enrollment']).reshape(-1, 1))
    df['International']= data['International'],
    df['Curricular_units_1st_sem_credited'] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(data['Curricular_units_1st_sem_credited']).reshape(-1, 1))
    df['Curricular_units_1st_sem_enrolled'] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data['Curricular_units_1st_sem_enrolled']).reshape(-1, 1))
    df['Curricular_units_1st_sem_evaluations'] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data['Curricular_units_1st_sem_evaluations']).reshape(-1, 1))
    df['Curricular_units_1st_sem_approved'] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data['Curricular_units_1st_sem_approved']).reshape(-1, 1))
    df['Curricular_units_1st_sem_grade'] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data['Curricular_units_1st_sem_grade']).reshape(-1, 1))
    df['Curricular_units_1st_sem_without_evaluations'] = scaler_Curricular_units_1st_sem_without_evaluations.transform(np.asarray(data['Curricular_units_1st_sem_without_evaluations']).reshape(-1, 1))
    df['Curricular_units_2nd_sem_credited'] = scaler_Curricular_units_2nd_sem_credited.transform(np.asarray(data['Curricular_units_2nd_sem_credited']).reshape(-1, 1))
    df['Curricular_units_2nd_sem_enrolled'] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data['Curricular_units_2nd_sem_enrolled']).reshape(-1, 1))
    df['Curricular_units_2nd_sem_evaluations'] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data['Curricular_units_2nd_sem_evaluations']).reshape(-1, 1))
    df['Curricular_units_2nd_sem_approved'] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data['Curricular_units_2nd_sem_approved']).reshape(-1, 1))
    df['Curricular_units_2nd_sem_grade'] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data['Curricular_units_2nd_sem_grade']).reshape(-1, 1))
    df['Curricular_units_2nd_sem_without_evaluations'] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data['Curricular_units_2nd_sem_without_evaluations']).reshape(-1, 1))
    df['Unemployment_rate'] = scaler_Unemployment_rate.transform(np.asarray(data['Unemployment_rate']).reshape(-1, 1))
    df['Inflation_rate'] = scaler_Inflation_rate.transform(np.asarray(data['Inflation_rate']).reshape(-1, 1))
    df['GDP'] = scaler_GDP.transform(np.asarray(data['GDP']).reshape(-1, 1))
    
    return df

    # df['Admission_grade'] = scaler_Admission_grade.transform(np.array([[data['Admission_grade']]]))[0, 0]
    # df['Curricular_units_1st_sem_approved'] = scaler_Curricular_units_1st_sem_approved.transform(np.array([[data['Curricular_units_1st_sem_approved']]]))[0, 0]
    # df['Curricular_units_1st_sem_credited'] = scaler_Curricular_units_1st_sem_credited.transform(np.array([[data['Curricular_units_1st_sem_credited']]]))[0, 0]
    # df['Curricular_units_1st_sem_enrolled'] = scaler_Curricular_units_1st_sem_enrolled.transform(np.array([[data['Curricular_units_1st_sem_enrolled']]]))[0, 0]
    # df['Curricular_units_1st_sem_evaluations'] = scaler_Curricular_units_1st_sem_evaluations.transform(np.array([[data['Curricular_units_1st_sem_evaluations']]]))[0, 0]
    # df['Curricular_units_1st_sem_grade'] = scaler_Curricular_units_1st_sem_grade.transform(np.array([[data['Curricular_units_1st_sem_grade']]]))[0, 0]
    # df['Curricular_units_1st_sem_without_evaluations'] = scaler_Curricular_units_1st_sem_without_evaluations.transform(np.array([[data['Curricular_units_1st_sem_without_evaluations']]]))[0, 0]
    # df['Curricular_units_2nd_sem_approved'] = scaler_Curricular_units_2nd_sem_approved.transform(np.array([[data['Curricular_units_2nd_sem_approved']]]))[0, 0]
    # df['Curricular_units_2nd_sem_credited'] = scaler_Curricular_units_2nd_sem_credited.transform(np.array([[data['Curricular_units_2nd_sem_credited']]]))[0, 0]
    # df['Curricular_units_2nd_sem_enrolled'] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.array([[data['Curricular_units_2nd_sem_enrolled']]]))[0, 0]
    # df['Curricular_units_2nd_sem_evaluations'] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.array([[data['Curricular_units_2nd_sem_evaluations']]]))[0, 0]
    # df['Curricular_units_2nd_sem_grade'] = scaler_Curricular_units_2nd_sem_grade.transform(np.array([[data['Curricular_units_2nd_sem_grade']]]))[0, 0]
    # df['Curricular_units_2nd_sem_without_evaluations'] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.array([[data['Curricular_units_2nd_sem_without_evaluations']]]))[0, 0]
    # df['GDP'] = scaler_GDP.transform(np.array([[data['GDP']]]))[0, 0]
    # df['Inflation_rate'] = scaler_Inflation_rate.transform(np.array([[data['Inflation_rate']]]))[0, 0]
    # df['Previous_qualification_grade'] = scaler_Previous_qualification_grade.transform(np.array([[data['Previous_qualification_grade']]]))[0, 0]
    # df['Unemployment_rate'] = scaler_Unemployment_rate.transform(np.array([[data['Unemployment_rate']]]))[0, 0]
    

print(gboost_model.feature_names_in_)