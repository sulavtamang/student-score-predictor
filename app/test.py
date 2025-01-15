import csv
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


unrefined_data= pd.read_csv('exams.csv')
unrefined_data
keep_col = ['math score', 'reading score', 'writing score']
new_f = unrefined_data[keep_col]
new_f.to_csv("newFile.csv", index=False)
updated_data_1 = pd.read_csv('newFile.csv')
updated_data_1

updated_data_1['percentage'] = (updated_data_1['math score'] + updated_data_1['reading score'] + updated_data_1['writing score'])/3
print(updated_data_1)

updated_data_1['study time']= updated_data_1['percentage']/6
updated_data_1['study time'] = updated_data_1['study time'].astype(int)
print(updated_data_1)

X= updated_data_1[['study time']]
y =updated_data_1['percentage']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state=102)
X_train
y_train
# Create and train a Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train) # Training the model

# # Make predictions
y_pred = linear_model.predict(X_test)
# Create one folder, virtual environment, pip install streamlit, Welcome to Salary Recommender App, user age print (age)



# Visualize the regression line
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', alpha=0.7, label='Actual')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.title("Linear Regression: Study hours per day  vs Percentage")
plt.xlabel("Study hours per day")
plt.ylabel("Percentage")
plt.legend()
plt.show()

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

import joblib
joblib.dump(linear_model, 'random training challange.pkl')
