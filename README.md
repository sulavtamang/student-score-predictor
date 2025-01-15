# Student Score Predictor

A simple web application built with **Streamlit** to predict the score of a student based on the number of hours they study. This project uses a linear regression model trained on a custom dataset.

---

## 📍 Features

- **📊 Input Study Hours**: Enter the number of hours you study.
- **📈 Predict Score**: The app predicts the score based on the input using a trained linear regression model.
- **🎨 User-Friendly UI**: Clean, visually appealing design with simple input fields and intuitive buttons.
- **🌍 Social Links**: Footer with links to the creator's social profiles.

---

## 🔧 Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Framework for building the web app.
- **Joblib**: For saving and loading the trained model.
- **NumPy**: For numerical operations.

---

## 🛠️ Installation

### 1. Clone the Repository:
```bash
git clone https://github.com/yourusername/student-score-predictor.git
cd student-score-predictor
```

### 2. Create and Activate Virtual Environment:
```cmd
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```
### 3. Install Dependencies:
```cmd
pip install -r requirements.txt
```

# 🚀 Usage
### Running the Project:
**1. Navigate to the app directory:**
```cmd
cd app
```

**2. Run the main script:**
```cmd
streamlit run app.py
```

**Your Streamlit app will open in a web browser, where you can input study hours and get the predicted score!**


# 📂 Project Structure
student-score-predictor/ ├── app/ # Application logic │ └── app.py # Main Streamlit app script ├── assets/ # Static assets (images, styles) │ └── images/ # Images and screenshots ├── datasets/ # Data files │ └── data.csv # Dataset used for training ├── env/ # Virtual environment files ├── models/ # Machine learning models │ └── linear_regression_model.pkl # Trained regression model saved using joblib ├── src/ # Source code for training and utilities │ └── model.py # Script for training the linear regression model ├── LICENSE # License information ├── README.md # Project documentation └── requirements.txt # Python dependencies for the project    

# 👨‍💻 Creator
***Sulav Man Sing Tamang***

- [GitHub](https://github.com/sulavtamang)
- [LinkedIn](https://www.linkedin.com/in/sulav-man-sing-tamang-269bb5190/)

# 🚀 Future Enhancements
- **📊 Data Visualization:** Add visualizations for scores and study hours.
- **🔄 Model Retraining:** Implement a feature to retrain the model with new data.
- **🌐 Cloud Deployment:** Deploy the app on a cloud platform like Heroku or AWS for public access.

# 📝 License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/sulavtamang/student-score-predictor/blob/main/LICENSE) file for more details.
