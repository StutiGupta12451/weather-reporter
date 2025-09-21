import streamlit as st
import numpy as np
from keras.models import load_model
model=load_model("weather_pred.h5")
def func1(arr):
    ans=model.predict(arr.reshape(1,-1))
    a=np.argmax(ans)
    #{0: 'drizzle', 1: 'fog', 2: 'rain', 3: 'snow', 4: 'sun'}
    if a==0:
        return "drizzle"
    elif a==1:
        return 'fog'
    elif a==2:
        return 'rain'
    elif a==3:
        return 'snow'
    elif a==4:
        return "sun"
st.title("Weather Predictor")
st.header("Enter info to predict weather")
prec=st.number_input("Enter precipitation")
temp_max=st.number_input("Enter Maximum Temperature")
temp_min=st.number_input("Enter Minimum Temperature")
wind=st.number_input("Enter Wind")
arr=np.array([prec,temp_max,temp_min,wind])
ans=func1(arr)
st.success("Accuracy is 82.60%")
final="Predicted weather is: "+ans
if st.button("Predict"):
    st.success(final)
