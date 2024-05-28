import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)  # This function return the number os columns objects that it receives as parameters

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Gabriel Ihmaid")
    content1 = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non facilisis mi, at cursus ex.
     Nullam dui felis, fringilla sed pharetra vitae, scelerisque eu mi. Maecenas imperdiet velit ultrices dictum ornare.
      Nunc tincidunt nisi eget pulvinar sollicitudin et faucibus est.
    """
    st.write(content1)

content2 = """
Below you can find some of the app i have built in Python. Feel free to contact me!
"""
st.write(content2)
