
import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
# import textract
from PyPDF2 import PdfFileReader
import pdfplumber

import os

# Function to save files
def save_uploaded_file(uploaded_file):
    with open(os.path.join('tempDir',uploaded_file.name),'wb') as f:
        f.write(uploaded_file.getbuffer())
        return st.success('File: {} Saved Successfuly in tempDir Folder'.format(uploaded_file.name))

def read_pdf(myfile):
    pdfReader = PdfFileReader(myfile)
    count = pdfReader.numPages
    all_pages_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_pages_text +=page.extractText()
        
    return all_pages_text



@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img




def main():
    st.title('How to Upload a File ! ')
    
    menu = ['Home','Datasets','Document Files', 'About']
    choice = st.sidebar.selectbox('Menu',menu)
    
    if choice =='Home':
        st.subheader('Home')
        
        image_file = st.file_uploader('Upload an Image', type = ['png','jpeg','jpg'])
        if image_file is not None:
            st.write(type(image_file))
            #st.write(dir(image_file))
            file_details = {
                'filename':image_file.name,
                'filetype': image_file.type,
                'filesize':image_file.size
            }
            st.write(file_details)
            st.image(load_image(image_file))
            # Saving Files
            save_uploaded_file(image_file)
            
            
    elif choice == 'Datasets':
        st.subheader('Datasets')
        data_file = st.file_uploader('Upload a CSV File', type = ['csv'])
        if data_file is not None:
            st.write(type(data_file)) 
            file_details = {
                'filename':data_file.name,
                'filetype': data_file.type,
                'filesize':data_file.size
            }
            st.write(file_details)
            df = pd.read_csv(data_file)
            st.dataframe(df)
            save_uploaded_file(data_file)
            
            
    elif choice == 'Document Files':
        st.subheader('Document File')
        doc_file = st.file_uploader('Upload Doc File', type = ['docx','pdf','txt'])
        if st.button('Process'):
            if doc_file is not None:
                file_details = {
                'filename':doc_file.name,
                'filetype': doc_file.type,
                'filesize':doc_file.size
            }
            st.write(file_details)
            if doc_file.type =='text/plain':
                # Read as Bytes
                # raw_text = doc_file.read() # Going read as bytes
                raw_text = str(doc_file.read(),'utf-8')
                st.write(raw_text)
                st.text('Below one is better')
                st.text(raw_text)
                # save_uploaded_file(raw_text)
                
            elif doc_file.type == 'application/pdf':
                try:
                    with pdfplumber.open(doc_file) as f:
                        pages = f.pages[0]
                        st.write(pages.extract_text())
                except:
                    st.write('You have an errro in pdf')
                    
                    
            # Using pypdf
                st.header('Using pypdf')
                raw_text = read_pdf(doc_file)
                st.write(raw_text)
                # save_uploaded_file(raw_text)
            else:
                raw_text = docx2txt.process(doc_file)
                st.write(raw_text)
                st.text(raw_text)
                save_uploaded_file(raw_text)
             # 
             
            
                
        
    else:
        st.subheader('About')      
    
    
    
if __name__=='__main__':
    main()