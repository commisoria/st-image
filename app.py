import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown('<h1> Loopx Image Editor</h1>',unsafe_allow_html=True)
st.markdown('---')
image=st.file_uploader('upload the file',type=['jpeg','jpg','png'])
size=st.empty()
mode=st.empty()
format=st.empty()
info=st.empty()
if image:
    img=Image.open(image)
    size.markdown(f"size: {img.size}")
    mode.markdown(f"mode: {img.mode}")
    info.markdown(f"mode: {img.info}")
    format.markdown(f"format: {img.format}")
    st.markdown('<h3> Resizing </h3>',unsafe_allow_html=True)
    width=st.number_input('width:',value=img.width)
    height=st.number_input('height:',value=img.height)
    st.markdown('<h3>Rotation</h3>',unsafe_allow_html=True)
    degree = st.number_input('degree:')
    st.markdown('<h3> Filters </h3>', unsafe_allow_html=True)
    filters=st.selectbox('Filters',options=('None','Blur','Contour','Detail','Emboss','Smooth'))
    button=st.button("Submit")
    if button:
        edited=img.resize((width,height)).rotate(degree)


        if filters!="None":
            if filters=='Blur':
                filtered=edited.filter(BLUR)
            elif filters=='Detail':
                filtered=edited.filter(DETAIL)
            elif filters=='Contour':
                filtered=edited.filter(CONTOUR)
            elif filters=='Emboss':
                filtered=edited.filter(EMBOSS)
            else:
                filtered=edited.filter(SMOOTH)
        st.image(edited)

