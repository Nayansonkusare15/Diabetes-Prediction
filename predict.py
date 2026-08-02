import joblib
import numpy as np

model = joblib.load("../model/diabetes_model.pkl")

print("Enter Patient Details")

Pregnancies = float(input("Pregnancies: "))
Glucose = float(input("Glucose: "))
BloodPressure = float(input("Blood Pressure: "))
SkinThickness = float(input("Skin Thickness: "))
Insulin = float(input("Insulin: "))
BMI = float(input("BMI: "))
DiabetesPedigreeFunction = float(input("Diabetes Pedigree Function: "))
Age = float(input("Age: "))

sample = np.array([[
    Pregnancies,
    Glucose,
    BloodPressure,
    SkinThickness,
    Insulin,
    BMI,
    DiabetesPedigreeFunction,
    Age
]])

prediction = model.predict(sample)

if prediction[0] == 1:
    print("\nPatient is likely Diabetic")
else:
    print("\nPatient is NOT Diabetic")
    