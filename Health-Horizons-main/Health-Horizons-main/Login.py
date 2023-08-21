# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 19:05:12 2023

@author: ASUS
"""

import streamlit as st
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
import subprocess
import webbrowser

url = 'https://health-horizon.onrender.com/'

# Connect to MongoDB
#client = MongoClient("mongodb://localhost:27017/")
client = MongoClient("mongodb+srv://manojmahato08779:a6TL0Yvo7OT3eiiv@cluster0.dk5pa5w.mongodb.net/?retryWrites=true&w=majority")
db = client["mydatabase"]
users = db["users"]
#my_list = ["streamlit", "run", "Main.py"]  # 👈️ list

# Login Function
def login():
    st.title("Login App")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = users.find_one({"username": username})
        if user and pbkdf2_sha256.verify(password, user["password"]):
            st.success("Logged in as {}".format(username))
            
            if st.button('Open browser'):
                webbrowser.open_new_tab(url)

            # Run the Main.py file as a separate process
            subprocess(["streamlit", "run", "Main.py"])
            process = subprocess.run(command, capture_output=True, text=True)

            # Print the output of the Main.py app
            st.write("Output from Main.py:\n{}".format(process.stdout))

            # Exit the current Streamlit app process
            raise SystemExit
        else:
            st.error("Incorrect username or password")


# Signup Function
def signup():
    st.title("Signup App")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Signup"):
        if users.find_one({"username": username}):
            st.error("Username already exists")
        else:
            hashed_password = pbkdf2_sha256.hash(password)
            users.insert_one({"username": username, "password": hashed_password})
            st.success("Account created")

# Streamlit App
def app():
    #st.title("Login/Signup App")
    menu = ["Signup", "Login"]
    choice = st.sidebar.selectbox("Select an option", menu)
    if choice == "Login":
        login()
    elif choice == "Signup":
        signup()

if __name__ == "__main__":
    app()
