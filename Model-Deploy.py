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
  
  st.markdown('<p style="font-family:Courier; color:Black; font-size: 15px;">Center class</p>')
  image=Image.open(center_path+'0.png')
  st.image(image, caption="<b>Class: center</b>")


