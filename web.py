import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Okoma Franklin")
    content = """ My name is Okoma Franklin Chukwuma i am a student of Delta State University
    Abraka, i am 23 years of age and i want to be a great pythom programmer and also impact much
    of this knowledge on people around my vasinity
    """
    st.info(content)

st.write("Below you can find some of the apps i have built on python")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep = ";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")







