import streamlit as st



def main():
    pass
# Title
st.title('Getting Started With StreamLit')

# Header
st.header('Goign to be Awesome')

# Subheader
st.subheader('Lets Rock!!')

# Text
st.text('This is my 1st streamlit text')
st.text('{} You are just getting started'.format('Nitin'))

# Creating a variable
myvar = 'Clients'
st.text('{} are going to like it'.format(myvar))

# Using Markdown
st.markdown('Hello World')
st.markdown('## Hello World')
st.markdown('# Hello World')

# Displaying Colored Text

# Success
st.success('It is Successful')

# Warning
st.warning('I am giving you last warning')

# Information
st.info(' Just another information Dude!!')

# Error
st.error('You are keep getting an errors QUIT!!')

# Exception
st.exception('This is an exception')

# SUperFunctions

# Notmal text
st.write('Hello Dude!!')

# Markdown
st.write('# Hello Dude!!')

# Python Code
st.write(12*2)
st.write('Hello'+'   Nitin!!')

st.write(dir(st))

# Getting Help
st.help(range)

if __name__ =='__main__':
    main()