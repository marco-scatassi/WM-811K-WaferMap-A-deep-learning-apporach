import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

from tensorflow import keras

center_path = 'Image_for_deploy/Center/'
donut_path = 'Image_for_deploy/Donut/'
edgeLoc_path = 'Image_for_deploy/Edge-Loc/'
edgeRing_path = 'Image_for_deploy/Edge-Ring/'
loc_path = 'Image_for_deploy/Loc/'
edgeLoc_path = 'Image_for_deploy/Edge-Loc/'
nearFull_path = 'Image_for_deploy/Near-full/'
random_path = 'Image_for_deploy/Random/'
scratch_path = 'Image_for_deploy/Scratch/'
none_path = 'Image_for_deploy/none/'

paths = [center_path,
  donut_path,
  edgeLoc_path,
  edgeRing_path,
  loc_path,
  edgeLoc_path,
  nearFull_path,
  random_path,
  scratch_path,
  none_path]

failureTypes = ['Center',
  'Donut',
  'Edge-Loc',
  'Edge-Ring',
  'Loc',
  'Edge-Loc',
  'Near-full',
  'Random',
  'Scratch',
  'none']

imagesDisplay = dict()
imagesDeploy = dict()

for i in range(len(failureTypes)):
  imagesDeploy[failureTypes[i]] = []
  imagesDisplay[failureTypes[i]] = []
  for j in range(10):
    image = tf.keras.utils.load_img(paths[i]+str(j)+'.png')
    imagesDeploy[failureTypes[i]].append(image)
    image = image.resize((100, 100))
    imagesDisplay[failureTypes[i]].append(image)
    
model_path = 'Models/model0_1'
model = keras.models.load_model(model_path)
  

st.set_page_config(layout = "wide")

p = np.empty([1,9])

def prediction(im):
  im = np.asarray(im)
  im = np.expand_dims(im, axis=0)
  global p
  p = model.predict(im)

if __name__ == '__main__':
  st.title("WM-811K WaferMap")
  st.write("Model evaluation for semiconductor wafermap detection and recognition using CNNs.")
  
  col1, col2 = st.columns([1,5])
  
  with col1:
    st.subheader("Failure Types")
    selectedType = st.selectbox("", failureTypes)
    st.write("")
  
  col1, col2, col3, col4, col5 = st.columns(5)
  cols = [col1, col2, col3, col4, col5]
  
  buttons = []
  
  for i in range(len(cols)):
    with cols[i]:
      st.image(imagesDisplay[selectedType][i])
      buttons.append(st.button('Image '+str(i), on_click = prediction, args = (imagesDeploy[selectedType][i],)))
      st.write('##')
      st.image(imagesDisplay[selectedType][i+5])
      buttons.append(st.button('Image '+str(i+5), on_click = prediction, args = (imagesDeploy[selectedType][i+5],)))
      
  if(np.sum(buttons) > 0): 
    st.write(p)
