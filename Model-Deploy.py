import streamlit as st
from PIL import Image

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

images = dict()

for i in range(len(failureTypes)):
  images[failureTypes[i]] = []
  for j in range(10):
    image = Image.open(paths[i]+str(j)+'.png')
    image = image.resize((100, 100))
    images[failureTypes[i]].append(image)
  

st.set_page_config(layout = "wide")


if __name__ == '__main__':
  st.title("WM-811K WaferMap")
  st.write("Model evaluation for semiconductor wafermap detection and recognition using CNNs.")
  
  col1, col2 = st.columns([1,4])
  
  with col1:
    st.selectbox("Failure Types", failureTypes)
  
  col1, col2, col3, col4, col5 = st.columns(5)
  cols = [col1, col2, col3, col4, col5]
  
  for i in range(len(cols)):
    with cols[i]:
      st.image(images['Center'][i])
      st.image(images['Center'][i+5])
