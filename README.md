# 🩺 Diabetes Prediction using Random Forest

A Machine Learning project that predicts whether a patient is likely to have diabetes based on various medical attributes. This project uses the **Random Forest Classification** algorithm from Scikit-learn to train a predictive model and classify patients as diabetic or non-diabetic.

---

## 📌 Table of Contents

- Overview
- Features
- Dataset
- Technologies Used
- Project Structure
- How It Works
- Installation
- Usage
- Model Evaluation
- Future Improvements
- License
- Author

---

# 📖 Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help in timely diagnosis and treatment.

This project builds a Machine Learning model using the **Random Forest Classifier** to predict diabetes based on medical information such as glucose level, BMI, age, insulin level, and blood pressure.

---

# 🚀 Features

- Data preprocessing
- Train/Test split
- Random Forest Classification
- Model Evaluation
- Save trained model
- Predict diabetes for new patients
- Simple command-line interface
- Well-commented and modular code

---

# 📊 Dataset

This project uses the **Pima Indians Diabetes Dataset**.

### Features

| Feature | Description |
|----------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-Hour serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Age of the patient |

### Target

| Value | Meaning |
|--------|---------|
| 0 | Non-Diabetic |
| 1 | Diabetic |

---

# 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

# 📁 Project Structure

```
Diabetes-Prediction/
│
├── dataset/
│   └── diabetes.csv
│
├── model/
│   └── diabetes_model.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   └── utils.py
│
├── notebook/
│   └── Diabetes_Prediction.ipynb
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

# ⚙️ How It Works

## Step 1: Load Dataset

The dataset is loaded using Pandas.

```python
data = pd.read_csv("dataset/diabetes.csv")
```

---

## Step 2: Split Dataset

The dataset is divided into:

- 80% Training Data
- 20% Testing Data

```python
train_test_split()
```

---

## Step 3: Train the Model

The project uses the **Random Forest Classifier**.

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

The model learns patterns from the training data.

---

## Step 4: Evaluate

After training, the model predicts the test data and calculates:

- Accuracy
- Confusion Matrix
- Classification Report

---

## Step 5: Save Model

The trained model is saved using Joblib.

```python
joblib.dump(model,"model/diabetes_model.pkl")
```

---

## Step 6: Prediction

The user enters patient details.

Example:

```
Pregnancies: 2
Glucose: 130
Blood Pressure: 70
Skin Thickness: 20
Insulin: 90
BMI: 28.4
Diabetes Pedigree Function: 0.4
Age: 32
```

Output

```
Patient is NOT Diabetic
```

or

```
Patient is likely Diabetic
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Diabetes-Prediction.git
```

Move into the project directory

```bash
cd Diabetes-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

### Train the Model

```bash
python src/train.py
```

---

### Evaluate Model

```bash
python src/evaluate.py
```

---

### Predict Diabetes

```bash
python src/predict.py
```

Enter the patient's medical details when prompted.

---

# 📈 Model Evaluation

The project evaluates the model using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# 🔮 Future Improvements

- Build a Flask web application
- Add Streamlit interface
- Hyperparameter tuning
- Feature scaling
- Deploy using Render or Hugging Face Spaces
- Docker support
- REST API integration

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```
git checkout -b feature-name
```

3. Commit your changes

```
git commit -m "Added new feature"
```

4. Push

```
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Nayan Sonkusare

B.Tech Computer Science (AI & ML)

Parul University

GitHub: https://github.com/Nayansonkusare15

LinkedIn: https://linkedin.com/in/NayanSonkusare

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
