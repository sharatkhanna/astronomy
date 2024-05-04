import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
content1 = """
A leading technology consulting firm based in San Francisco, CA, 
specializing in [specific technology expertise]. 
We provide innovative solutions to businesses of all sizes, 
with a track record of success spanning [number of years] years. We help our 
clients navigate the complexities of the digital landscape and achieve their 
goals efficiently and effectively. 

"""
st.write(content1)
st.header("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1, 0.75, 1, 0.75, 1])

df = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        name = (row["first name"] + " " + row["last name"])
        st.subheader(name.title())
        st.write(row['role'])
        st.image("images/" + row['image'])
        st.write(" ")

with col2:
    for index, row in df[4:8].iterrows():
        name = (row["first name"] + " " + row["last name"])
        st.subheader(name.title())
        st.write(row['role'])
        st.image("images/" + row['image'])
        st.write(" ")

with col3:
    for index, row in df[8:].iterrows():
        name = (row["first name"] + " " + row["last name"])
        st.subheader(name.title())
        st.write(row['role'])
        st.image("images/" + row['image'])
        st.write(" ")