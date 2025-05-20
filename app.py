import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing
from prediction import prediction


st.title("Student Dropout & Graduation Prediction")


col1, col2, col3 = st.columns(3)
with col1:
    Marital_status = st.selectbox(label='Marital status', options=[0, 1, 2, 3])
    # data['Marital_status'] = Marital_status
with col2:
    Application_mode = int(st.number_input(label='Application mode', value=1, max_value=12, min_value=0))
    # data['Application_mode'] = Application_mode
with col3:
    Application_order = int(st.number_input(label='Application order', value=1, max_value=9, min_value=0))
    # data['Application_order'] = Application_order
    
col1, col2, col3 = st.columns(3)
with col1:
    Admission_grade = float(st.slider("Admission grade", min_value=0, max_value=200, step=1))
    # data['Admission_grade'] = Admission_grade
with col2:
    Course = st.slider("Course", min_value=0, max_value=14, step=1)
    # data['Course'] = Course
with col3:
    Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=[1, 0])
    # data['Daytime_evening_attendance'] = Daytime_evening_attendance
    
col1, col2, col3, col4 = st.columns(4)
with col1:
    Nacionality = st.selectbox(label='Nacionality', options=[1, 0])
    # data['Nacionality'] = Nacionality
with col2:
    Previous_qualification = int(st.number_input(label='Previous qualification', value=1, min_value=0, max_value=11))
    # data['Previous_qualification'] = Previous_qualification
with col3:
    Previous_qualification_grade = float(st.slider("Previous qualification grade", min_value=0, max_value=20, step=1)) 
    # data['Previous_qualification_grade'] = Previous_qualification_grade 
with col4:
    Gender = st.selectbox(label="Gender", options=[1, 0])
    # data['Gender'] = Gender
        
col1, col2, col3 = st.columns(3)
with col1:
    Debtor = st.selectbox(label='Debtor', options=[1, 0])
    # data['Debtor'] = Debtor
with col2:
    Displaced = st.selectbox(label='Displaced', options=[1, 0])
    # data['Displaced'] = Displaced
with col3:
    Educational_special_needs = st.selectbox(label='Education special', options=[1, 0])
    # data['Educational_special_needs'] = Educational_special_needs
    
col1, col2, col3, col4 = st.columns(4)
with col1:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition fee', options=[1, 0])
    # data['Tuition_fees_up_to_date'] = Tuition_fees_up_to_date
with col2:
    Scholarship_holder = st.selectbox(label='Scholarship', options=[1, 0])
    # data['Scholarship_holder'] = Scholarship_holder
with col3:
    Age_at_enrollment = st.number_input(label='Age', value=18, min_value=10, max_value=100)
    # data['Age_at_enrollment'] = Age_at_enrollment
with col4:
    International = st.selectbox(label='International', options=[1, 0])
    # data['International'] = International
    
col1, col2, col3 = st.columns(3)
with col1:
    Unemployment_rate = float(st.slider(label='Unemployment rate', value=0.0, min_value=-100.0, max_value=100.0))
    # data['Unemployment_rate'] = Unemployment_rate
with col2:
    Inflation_rate = float(st.slider(label='Inflation rate', value=0.0, min_value=-100.0, max_value=100.0))
    # data['Inflation_rate'] = Inflation_rate
with col3:
    GDP = float(st.slider(label='GDP', value=0.0, min_value=-100.0, max_value=100.0))
    # data['GDP'] = GDP

col1, col2 = st.columns(2)
with col1:
    Fathers_occupation = st.slider(label='Fathers occupation', min_value=0, max_value=12, step=1)
    # data['Fathers_occupation'] = Fathers_occupation
with col2:
    Mothers_occupation = st.slider(label='Mothers occupation', min_value=0, max_value=10, step=1)
    # data['Mothers_occupation'] = Mothers_occupation

col1, col2 = st.columns(2)
with col1:
    Mothers_qualification = st.slider(label='Mothers qualification', min_value=0, max_value=12, step=1)
    # data['Mothers_qualification'] = Mothers_qualification
with col2:
    Fathers_qualification = st.slider(label='Fathers qualification', min_value=0, max_value=12, step=1)
    # data['Fathers_qualification'] = Fathers_qualification
    
col1, col2, col3, col4 = st.columns(4)
with col1:
    Curricular_units_1st_sem_credited = st.number_input("Curricular_units_1st_sem_credited", min_value=0, max_value=20)
    # data['Curricular_units_1st_sem_credited'] = Curricular_units_1st_sem_credited
with col2:
    Curricular_units_1st_sem_enrolled = st.number_input("Curricular_units_1st_sem_enrolled", min_value=0, max_value=26)
    # data['Curricular_units_1st_sem_enrolled'] = Curricular_units_1st_sem_enrolled
with col3:
    Curricular_units_1st_sem_evaluations = st.number_input("Curricular_units_1st_sem_evaluations", min_value=0, max_value=45)
    # data['Curricular_units_1st_sem_evaluations'] = Curricular_units_1st_sem_evaluations
with col4:
    Curricular_units_1st_sem_approved = st.number_input("Curricular_units_1st_sem_approved", min_value=0, max_value=26)
    # data['Curricular_units_1st_sem_approved'] = Curricular_units_1st_sem_approved

col1, col2 = st.columns(2)
with col1:
    Curricular_units_1st_sem_grade = float(st.slider(label='Curricular_units_1st_sem_grade', value=0.0, min_value=0.0, max_value=20.0))
    # data['Curricular_units_1st_sem_grade'] = Curricular_units_1st_sem_grade
with col2:
    Curricular_units_1st_sem_without_evaluations = st.number_input("Curricular_units_1st_sem_without_evaluations", min_value=0, max_value=12)
    # data['Curricular_units_1st_sem_without_evaluations'] = Curricular_units_1st_sem_without_evaluations
    

col1, col2, col3, col4 = st.columns(4)
with col1:
    Curricular_units_2nd_sem_credited = st.number_input("Curricular_units_2nd_sem_credited", min_value=0, max_value=19)
    # data['Curricular_units_2nd_sem_credited'] = Curricular_units_2nd_sem_credited
with col2:
    Curricular_units_2nd_sem_enrolled = st.number_input("Curricular_units_2nd_sem_enrolled", min_value=0, max_value=21)
    # data['Curricular_units_2nd_sem_enrolled'] = Curricular_units_2nd_sem_enrolled
with col3:
    Curricular_units_2nd_sem_evaluations = st.number_input("Curricular_units_2nd_sem_evaluations", min_value=0, max_value=33)
    # data['Curricular_units_2nd_sem_evaluations'] = Curricular_units_2nd_sem_evaluations
with col4:
    Curricular_units_2nd_sem_approved = st.number_input("Curricular_units_2nd_sem_approved", min_value=0, max_value=20)
    # data['Curricular_units_2nd_sem_approved'] = Curricular_units_2nd_sem_approved

col1, col2 = st.columns(2)
with col1:
    Curricular_units_2nd_sem_grade = float(st.slider(label='Curricular_units_2nd_sem_grade', value=0.0, min_value=0.0, max_value=20.0))
    # data['Curricular_units_2nd_sem_grade'] = Curricular_units_2nd_sem_grade
with col2:
    Curricular_units_2nd_sem_without_evaluations = st.number_input("Curricular_units_2nd_sem_without_evaluations", min_value=0, max_value=12)
    # data['Curricular_units_2nd_sem_without_evaluations'] = Curricular_units_2nd_sem_without_evaluations


data = pd.DataFrame([{
    'Admission_grade': Admission_grade,
    'Marital_status': Marital_status,
    'Application_mode': Application_mode,
    'Application_order': Application_order,
    'Course': Course,
    'Daytime_evening_attendance': Daytime_evening_attendance,
    'Nacionality': Nacionality,
    'Previous_qualification': Previous_qualification,
    'Gender': Gender,
    'Debtor': Debtor,
    'Displaced': Displaced,
    'Educational_special_needs': Educational_special_needs,
    'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
    'Scholarship_holder': Scholarship_holder,
    'Age_at_enrollment': Age_at_enrollment,
    'International': International,
    'Fathers_occupation': Fathers_occupation,
    'Mothers_occupation': Mothers_occupation,
    'Mothers_qualification': Mothers_qualification,
    'Fathers_qualification': Fathers_qualification,
    'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
    'Curricular_units_1st_sem_credited': Curricular_units_1st_sem_credited,
    'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
    'Curricular_units_1st_sem_evaluations': Curricular_units_1st_sem_evaluations,
    'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
    'Curricular_units_1st_sem_without_evaluations': Curricular_units_1st_sem_without_evaluations,
    'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
    'Curricular_units_2nd_sem_credited': Curricular_units_2nd_sem_credited,
    'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
    'Curricular_units_2nd_sem_evaluations': Curricular_units_2nd_sem_evaluations,
    'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
    'Curricular_units_2nd_sem_without_evaluations': Curricular_units_2nd_sem_without_evaluations,
    'GDP': GDP,
    'Inflation_rate': Inflation_rate,
    'Previous_qualification_grade': Previous_qualification_grade,
    'Unemployment_rate': Unemployment_rate,
}])

# with st.expander("View the Raw Data"):
#     st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
        # prediction_result = prediction(new_data)
    st.write("Student Performance: {}".format(prediction(new_data)))