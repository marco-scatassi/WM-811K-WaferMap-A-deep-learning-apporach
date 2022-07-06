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


st.set_page_config(layout = "wide")


if __name__ == '__main__':
  st.title("WM-811K WaferMap")
  st.write("Model evaluation for semiconductor wafermap detection and recognition using CNNs.")
  
  st.markdown('<b>Center class</b>', unsafe_allow_html=True)
  
  for i in range(10):
   image = Image.open(center_path+str(i)+'.png')
   image = image.resize((600, 400))
   st.image(image)


