# 🥗 Local Food Wastage Management System

## 📌 Project Overview

Food wastage is a significant global issue — many households and restaurants discard surplus food while millions face hunger.

The **Local Food Wastage Management System** connects **surplus food providers** (restaurants, households) with **receivers** (NGOs, individuals in need) to minimize waste and improve food distribution.

This project uses **SQLite** for database management, **SQL queries** for analysis, and a **Streamlit web application** for easy interaction.

---

## 🎯 Features

- **Provider & Receiver Management** – Add and view details.
- **Food Listings** – Browse, filter, and view available food items.
- **Claims Management** – Record and track food claims.
- **Analytics Dashboard** – View insights such as:
  - Providers per city
  - Most common food types
  - Claim success rate by city
  - Items nearing expiry
- **Interactive Filters** – Filter data by city, provider, food type, and meal type.

---

## 🗂️ Project Structure

📁 local-food-wastage-management

```
│── app.py # Main Streamlit application entry point
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│
├── 📁 data # Data storage
│ │── food_listing_data.csv
│ │── claims_data.csv
│ │── providers_data.csv
│ │── receivers_data.csv
│
├── 📁 database # Database & schema
│ │── food_waste.db # SQLite database file
│ │── schema.sql # Database schema
│ │── queries.sql # Analytical SQL queries
│
├── 📁 notebooks # Jupyter notebooks
│ │── main.ipynb # Main analysis / prototyping notebook
```

---

---

## 🚀 Live Demo

Access the live web application here:  
**🔗 [Streamlit App](https://local-food-management-system.streamlit.app/)**

---

## 🛠️ Tech Stack

- **Python 3**
- **SQLite**
- **Pandas**
- **Streamlit**
- **SQL**

---

## 📊 SQL Queries

The project includes **15 analytical queries** to gain insights, such as:

1. Providers per city
2. Receivers per city
3. Top provider type by quantity
4. Receivers who claimed the most
5. Most common food types
6. Claim success rate by city
   ...and more.

---

## 💻 Running Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ---

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

---

3. Run the app

```bash
streamlit run app.py

```

---

4. Open in browser
   Streamlit will provide a local URL, usually http://localhost:8501.

---
