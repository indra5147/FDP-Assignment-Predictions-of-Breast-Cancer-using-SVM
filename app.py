
import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
pickle_in = open("/content/drive/My Drive/Assignment/data.pkl","rb")
model=pickle.load(pickle_in)
dataset= pd.read_csv('/content/drive/My Drive/Assignment/data.csv')

def predict_note_authentication(perimeter_mean, concave_points_mean, radius_se, perimeter_se, perimeter_worst, concave_points_worst):
  output= model.predict(([[perimeter_mean, concave_points_mean, radius_se, perimeter_se, perimeter_worst, concave_points_worst]]))
  print("diagnosis", output)
  if output==[1]:
    prediction="Malignant "
  else:
    prediction="Benign"
  print(prediction)
  return prediction
def main():
    
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;">Breast Cancer Detection</p></center> 
   </div>
   </div>
   </div>
   """

    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Breast Cancer Prediction")

    perimeter_mean = st.number_input("Insert Perimeter mean")
    concave_points_mean = st.number_input("Insert Concave points mean")
    radius_se = st.number_input("Insert Radius se")
    perimeter_se = st.number_input("Insert Perimeter se")
    perimeter_worst = st.number_input("Insert Perimeter worst")
    concave_points_worst = st.number_input("Insert Concave points worst")

    if st.button("Predict"):
      result=predict_note_authentication(perimeter_mean, concave_points_mean, radius_se, perimeter_se, perimeter_worst, concave_points_worst)
      st.success('Model has predicted {}'.format(result))

if __name__=='__main__':
  main()