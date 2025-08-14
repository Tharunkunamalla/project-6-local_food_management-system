
import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

DB_PATH = 'food_waste.db'

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def run_query(query, params=None):
    with get_conn() as conn:
        return pd.read_sql_query(query, conn, params=params or {})

def execute_query(query, params=None):
    with get_conn() as conn:
        conn.execute(query, params or {})
        conn.commit()

st.set_page_config(page_title="Local Food Wastage Management", page_icon="🥗", layout="wide")
st.title("🥗 Local Food Wastage Management System")

menu = ["Home", "Providers", "Receivers", "Food Listings", "Claims", "Analytics"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("Welcome!")
    st.write("This app connects surplus food providers with those in need, reducing food wastage.")

elif choice == "Providers":
    st.subheader("Manage Providers")
    df = run_query("SELECT * FROM providers")
    st.dataframe(df)
    with st.form("add_provider"):
        st.write("Add New Provider")
        pid = st.number_input("Provider ID", step=1)
        name = st.text_input("Name")
        ptype = st.text_input("Type")
        address = st.text_input("Address")
        city = st.text_input("City")
        contact = st.text_input("Contact")
        submitted = st.form_submit_button("Save")
        if submitted:
            execute_query(
                "INSERT INTO providers VALUES (?, ?, ?, ?, ?, ?)",
                (pid, name, ptype, address, city, contact)
            )
            st.success("Provider added successfully!")

elif choice == "Receivers":
    st.subheader("Manage Receivers")
    df = run_query("SELECT * FROM receivers")
    st.dataframe(df)

elif choice == "Food Listings":
    st.subheader("Browse Food Listings")
    city_filter = st.selectbox("City", ["All"] + run_query("SELECT DISTINCT Location FROM food_listings")["Location"].dropna().tolist())
    query = "SELECT * FROM food_listings"
    if city_filter != "All":
        query += " WHERE Location = :city"
        df = run_query(query, {"city": city_filter})
    else:
        df = run_query(query)
    st.dataframe(df)

elif choice == "Claims":
    st.subheader("Manage Claims")
    df = run_query("SELECT * FROM claims")
    st.dataframe(df)

elif choice == "Analytics":
    st.subheader("Analytics & Insights")
    q1 = run_query("SELECT City, COUNT(*) AS Provider_Count FROM providers GROUP BY City ORDER BY Provider_Count DESC;")
    st.write("Providers per City")
    st.dataframe(q1)
