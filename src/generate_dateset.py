import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Number of data points
n = 5000

# Generate random study hours between 0 and 24 hours
study_hours = np.random.uniform(0, 24, n).round(2)

# Simulate a non-linear relationship between study hours and scores
# Let's assume the relationship has a polynomial nature (quadratic)
# Adding noise to make it more realistic
# scores = 4 * study_hours + np.random.normal(0, 10, n)
scores = 4 * study_hours + np.random.normal(0, 5, n)  # Reduced noise


# Clip the scores to ensure they stay within the range of 0 to 100
scores = np.clip(scores, 0, 100).round(2)

# Create the DataFrame
data = pd.DataFrame({
    'Study Hours': study_hours,
    'Scores': scores
})

# Save the dataset to a CSV file
data.to_csv('./datasets/study_hours_scores.csv', index=False)
