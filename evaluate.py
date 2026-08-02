import pandas as pd
import joblib

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

data = pd.read_csv("../dataset/diabetes.csv")

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = joblib.load("../model/diabetes_model.pkl")

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))

print(confusion_matrix(y_test, predictions))
