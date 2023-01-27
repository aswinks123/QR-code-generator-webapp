from pathlib import Path

import PIL
import streamlit as st
from PIL import Image
import qrcode
import time
from pyzbar.pyzbar import decode
import cv2
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def qr_generator(url,foreground,background,col2):
    # Creating QR code using the provided data

    feature = qrcode.QRCode(version=1, box_size=20, border=1)
    feature.add_data(url)
    feature.make(fit=True)
    img = feature.make_image(fill_color=foreground, back_color=background)
    img.save("qr-image.jpg")


    with col2:
        with st.spinner('Creating your QR code...'):
            time.sleep(2)
        # st.success('Success')

        image = Image.open('qr-image.jpg')


        st.image(image)


def Generate_QR():

    st.title('Color QR - QR code maker')
    url = st.text_input('type the URL or text to generate QR code')
    col1, col2 = st.columns(2)
    with col1:
        allcolors = ['Black', 'Red', 'Blue', 'White', 'Yellow', 'Cyan', 'Magenta']
        allcolors2 = ['White', 'Black', 'Blue', 'Red', 'Yellow', 'Cyan', 'Magenta']

        st.header("Foreground color")

        foreground = st.selectbox(
            '',
            (allcolors))
        st.title("\n")

        st.header("Background color")

        background = st.selectbox(
            '',
            (allcolors2))

    col3, col4 = st.columns(2)
    with col3:
        if st.button('Generate'):
            if url == "":
                st.error('Please enter the text or URL', icon="🚨")
            elif foreground == background:
                st.error('Foreground and Background colors cannot be the same', icon="🚨")
            else:
                qr_generator(url, foreground, background,col2)

                with col4:

                    with open("qr-image.jpg", "rb") as file:
                        btn = st.download_button(
                            label="Download image",
                            data=file,
                            file_name="qr.png",
                            mime="image/png"
                        )








def page2():
    st.subheader("Scan QR-Code")

    uploaded_file =st.file_uploader("Upload a QR code", accept_multiple_files=False)




    if st.button("Decode"):
        try:

            if not uploaded_file is None:

                image = PIL.Image.open(uploaded_file)
                image.save('uploaded-qr.png')
                decode_image = cv2.imread('uploaded-qr.png')

                detector = cv2.QRCodeDetector()
                data= detector.detectAndDecode(decode_image)

                st.subheader("QR decoded successfully ")
                st.code(data[0], language='Python')

            else:
                st.error('Please choose an Image first', icon="🚨")
        except:
            st.error('Invalid file!', icon="🚨")


def page3():
    st.markdown("Created by Aswin KS")
    st.markdown("Thanks")


def Home():

    about="""
    Color-QR is a webapp for creaing QR codes. It is free and made entirly using Python.
    This app allows to generate QR codes and decode the content of existing QR codes!
    
    Choose an option from side bar to get started!
    
    
    """
    st.title("ColorQR online QR code generator")
    st.title("")
    st.title("")
    st.subheader(about)



page_names_to_funcs = {
    "Home": Home,
    "Generate-QR": Generate_QR,
    "Scan-QR": page2,
    "About": page3,
}
with st.sidebar:
    col1,col2=st.columns(2)
    with col1:
        image = Image.open('scan.png')
        st.image(image)
    st.title("Choose an option")
    #sidebar.header("Select an option")

selected_page = st.sidebar.selectbox("", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
