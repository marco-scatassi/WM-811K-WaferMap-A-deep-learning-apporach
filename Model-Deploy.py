import streamlit as st
import zipfile
from PIL import Image

zip = zipfile.ZipFile('ImageToDeploy')
zipName = zip.namelist()[0]
path = zip.extract(zipName)

st.set_page_config(layout = "wide")

if __name__ == '__main__':
  st.title("WM-811K WaferMap")
  st.write("Model evaluation for semiconductor wafermap detection and recognition using CNNs.")
  st.write(path)


