''' 
Experiment 1:
Implement and demonstrate the FIND-S algorithm for finding the most specific hypothesis based on a given set of training data samples.
Read the training data from a .CSV file.
'''

import pandas as pd
# Dataset link : https://www.kaggle.com/datasets/fredericobreno/play-tennis

# Load CSV from Google Drive
df = pd.read_csv("/content/play_tennis.csv")

X = df.drop('play', axis=1)
y = df['play']

# Initialize most specific hypothesis
hypothesis = ['0'] * len(X.columns)
print("Initial hypothesis : ", hypothesis)


# Step 1: Find first positive example
for i in range(len(X)):
    if y.iloc[i] == 'Yes':
        hypothesis = X.iloc[i].tolist()
        break
print("First positive hypothesis : ", hypothesis)

# Step 2: Generalize based on other positive examples
for i in range(len(X)):
    if y.iloc[i] == 'Yes':
        for j in range(len(X.columns)):
            if hypothesis[j] != X.iloc[i, j]:
                hypothesis[j] = '?'

print("Final Hypothesis:", hypothesis)
