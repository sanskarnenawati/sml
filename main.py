import streamlit as st
import numpy as np
import pickle
def predict(data):
    lr = pickle.load('rentpred.sav')
    return lr.predict(df)

st.title('Home rent prediction')

st.write('---')

# area of the house
area = st.slider('Area of the house', 1000, 5000, 1500)

# no. of bedrooms in the house
bedrooms = st.number_input('No. of bedrooms', min_value=0, step=1)




if st.button('Predict House Price'):
    cost = predict(np.array([[area, bedrooms]]))
    st.text(cost[0])