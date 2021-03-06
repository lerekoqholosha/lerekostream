# -*- coding: utf-8 -*-
"""streamlitapp.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19wbevp9TedyASucqfEalFPEs2XBAY7WM
"""

#!pip install streamlit

"""# Building Iris dataset streamlit app"""

#import libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

"""**Start bulding the app :)**"""

st.write(""" 
# Simple Iris Flower Prediction App

This app predicts **Iris Flower** type!

""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length',4.3,7.9,5.4)
    sepal_width = st.sidebar.slider('Sepal Width',2.0,4.4,3.4)
    petal_length = st.sidebar.slider('Petal Length',1.0,6.9,1.3)
    petal_width = st.sidebar.slider('Petal Width',0.1,2.5,0.2)

    #create a dataframe



    
    data = {'sepal_length':sepal_length,
            'sepal_width':sepal_width,
            'petal_length':petal_length,
            'petal_width': petal_width
        
    }

    features = pd.DataFrame(data,index=[0])
    return features

df = user_input_features()
st.subheader('User Input Parameters')
st.write(df)

#loading data from sklearn datasets
iris = datasets.load_iris()
X= iris.data
Y= iris.target

#creating randomforest classifier and making predictions
clf = RandomForestClassifier()
clf.fit(X,Y)


prediction = clf.predict(df)
prediction_prob = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_prob)