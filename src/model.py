import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import numpy as np


student_scores_df = pd.read_csv('./datasets/study_hours_scores.csv')


x = student_scores_df[['Study Hours']]
y = student_scores_df[['Scores']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

linear_model = LinearRegression()
linear_model.fit(x_train, y_train)

y_pred = linear_model.predict(x_test)

mse = mean_squared_error(x_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

import numpy as np
rmse = np.sqrt(mse)
print("Root Mean Squared Error (RMSE):", rmse)


joblib.dump(linear_model, './models/student_score_prediction_model.pkl')
