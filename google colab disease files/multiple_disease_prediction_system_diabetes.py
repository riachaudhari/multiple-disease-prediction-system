# -*- coding: utf-8 -*-
"""Multiple Disease Prediction System-Diabetes

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17FOFOMqiSTLnCXU4bTrvMOGCEDVtVbp6
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""**Data Collection and Analysis**"""

diabetes_dataset = pd.read_csv('/content/diabetes.csv')

diabetes_dataset.head()

diabetes_dataset.shape

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0-> Non Diabetic

1-> Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

"""People with glucose levels closer to 140,insulin levels higher and are of an older age are more likely to get diabetes"""

X=diabetes_dataset.drop(columns='Outcome',axis=1)
Y=diabetes_dataset['Outcome']

print(X)

print(Y)

"""Data Standardization"""

scaler=StandardScaler()

scaler.fit(X)

standardized_data=scaler.transform(X)

print(standardized_data) #all values are in range of -1 to 1

X=standardized_data
Y=diabetes_dataset['Outcome']

"""**Train Test split**"""

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""**Training model**"""

classifier=svm.SVC(kernel='linear')

#training the support vector machine classifier
classifier.fit(X_train,Y_train)

"""**Model Evaluation**

Accuracy Score
"""

#accuracy score on training data
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print('Accuracy score of training data:',training_data_accuracy)

#accuracy score on test data
X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

print('Accuracy score of test data:',test_data_accuracy)

"""**Building a predictive system**"""

input_data=(4,110,92,0,0,37.6,0.191,30)

#change input data to numpy array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

#standardize the inout data
std_data=scaler.transform(input_data_reshaped)
print(std_data)

prediction=classifier.predict(std_data)
print(prediction)

if (prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

input_data=(1,189,60,23,846,30.1,0.398,59)

#change input data to numpy array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

#standardize the inout data
std_data=scaler.transform(input_data_reshaped)
print(std_data)

prediction=classifier.predict(std_data)
print(prediction)

if (prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

import pickle

filename='diabetes_model.sav'
pickle.dump(classifier,open(filename,'wb'))

#loading the saved model
loaded_model=pickle.load(open('diabetes_model.sav','rb'))

