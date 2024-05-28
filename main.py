import streamlit as st
import pandas

st.set_page_config(layout="wide")

# This function return the number os columns objects that it receives as parameters
col1, col2 = st.columns(2)

# The with operator represents the actions that are include at certain column
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

# The list as argument represents the ratio of width of each column
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# The pandas function extract the data from csv archive and generates a legible object for python
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
