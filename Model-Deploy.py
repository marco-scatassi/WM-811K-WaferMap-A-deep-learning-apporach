import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import pandas 
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
  nearFull_path,
  random_path,
  scratch_path,
  none_path]

failureTypes = ['Center',
  'Donut',
  'Edge-Loc',
  'Edge-Ring',
  'Loc',
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

if 'all_pr' not in st.session_state:
  st.session_state.all_pr = ''
  
if 'class_pr' not in st.session_state:
  st.session_state.class_pr = ''

st.set_page_config(layout = "wide")

def prediction(im):
  im = np.asarray(im)
  im = np.expand_dims(im, axis=0)
  all_pr = model.predict(im)
  class_pr = failureTypes[np.argmax(all_pr)]
  print_all_pr = pandas.DataFrame(all_pr, columns=failureTypes)
  st.session_state.all_pr = print_all_pr
  st.session_state.class_pr = class_pr

if __name__ == '__main__':
  st.title("WM-811K WaferMap")
  st.subheader("Summary")
  st.markdown(
    "In this page is possible to play with a **CNN model** developed to approach the task of **semiconductor wafermaps failure detection and recognition**. " +
    "In particular, the problem consists in identify the type of defect of a specific wafermap among 9:\n" +
    "<p style='font-style: italic;text-align:center'> Center - Donut - Edge-Loc - Edge-Ring - Loc - Near-full - Random - Scratch - none </p>" + "\n" +
    "Selecting a type of failure will show you 10 images associated with that specific defect. Clicking the button under a certain image you can see the " +
    "<span style='font-weight:bold'> class predicted </span> for that image by the model and the" + 
    "<span style='font-weight:bold'> probability of belonging to each class </span> (i.e. the output of the model)."
    ,unsafe_allow_html=True
  )
  st.write("##")
  
  
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
  
  st.write('##')
  st.subheader("Probability to belong to a specific failure types class")
  for i in range(len(buttons)):
    if buttons[i]:
      st.session_state.all_pr

  st.subheader("Class predicted")
  for i in range(len(buttons)):
    if buttons[i]:
      st.session_state.class_pr
