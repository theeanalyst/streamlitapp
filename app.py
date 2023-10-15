# ----- Load base libraries and packages
import streamlit as st
import numpy as np
import pandas as pd
import re
import os
from PIL import Image
import base64
import pickle
from sklearn.ensemble import RandomForestClassifier 

# Function to load ML toolkit
def load_ml_toolkit(file_path=r"streamlit_toolkit"):
    with open(file_path, "rb") as file:
        loaded_toolkit = pickle.load(file)
    return loaded_toolkit

# Importing the toolkit
loaded_toolkit = load_ml_toolkit(r"streamlit_toolkit") 
encoder = loaded_toolkit["encoder"]
scaler = loaded_toolkit["scaler"]

# Load the saved Random Forest model from a file
with open('random_forest_model.pkl', 'rb') as model_file:
    loaded_rf_model = pickle.load(model_file)
    
# Set up the Streamlit app
st.title("Sales Prediction App")
st.write("This app uses machine learning to predict sales based on certain input parameters. Enter the details below and click 'Predict' to get a sales prediction!")

# Load and display an image
image = Image.open("grocery_shopping_woman.png")
st.image(image, width=600)

# Create input fields
input_data = {}

st.subheader("Enter the details to predict sales")

# Define categorical and numerical columns
categorical_columns = ['products', 'state', 'store_type', 'end_month']
numerical_columns = ['store_nbr', 'onpromotion', 'cluster', 'oil_price', 'year', 'month', 'dayofmonth', 'dayofweek']

# Create two columns for input fields
col1, col2 = st.columns(2)

# Input fields for categorical columns
with col1:
    input_data['products'] = st.selectbox("Product Category", ['AUTOMOTIVE', 'CLEANING', 'BEAUTY', 'FOODS', 'STATIONERY', 'CELEBRATION', 'GROCERY', 'HARDWARE', 'HOME', 'LADIESWEAR', 'LAWN AND GARDEN', 'CLOTHING', 'LIQUOR,WINE,BEER', 'PET SUPPLIES'])
    input_data['state'] = st.selectbox("State", ['Pichincha', 'Cotopaxi', 'Chimborazo', 'Imbabura', 'Santo Domingo de los Tsachilas', 'Bolivar', 'Pastaza', 'Tungurahua', 'Guayas', 'Santa Elena', 'Los Rios', 'Azuay', 'Loja', 'El Oro', 'Esmeraldas', 'Manabi'])
    input_data['store_type'] = st.selectbox("Store Type", ['D', 'C', 'B', 'E', 'A'])
    input_data['end_month'] = st.radio("Is it the end of the month?", ['True', 'False'])

# Input fields for numerical columns
with col2:
    input_data['store_nbr'] = st.slider("Store Number", 0, 54)
    input_data['onpromotion'] = st.number_input("On Promotion", step=1)
    input_data['cluster'] = st.number_input("Cluster", step=1)
    input_data['oil_price'] = st.number_input("oil_price", step=1)
    input_data['year'] = st.number_input("Year", step=1)
    input_data['month'] = st.slider("Month", 1, 12)
    input_data['dayofmonth'] = st.slider("Day", 1, 31)
    input_data['dayofweek'] = st.number_input("Day of Week (0=Sun, 1=Mon, ..., 6=Sat)", step=1)

# Create a button to make a prediction
if st.button("Predict", help="Click to make a prediction."):
    # Convert the input data to a pandas DataFrame
    input_df = pd.DataFrame([input_data])

    # Apply the imputers to categorical and numerical columns
    input_df_imputed_cat = pd.DataFrame(encoder.transform(input_df[categorical_columns]).toarray(), columns=encoder.get_feature_names(categorical_columns))
    input_df_imputed_num = pd.DataFrame(scaler.transform(input_df[numerical_columns]), columns=numerical_columns)

    # Make a prediction
    final_df = pd.concat([input_df_imputed_cat, input_df_imputed_num], axis=1)
    prediction = loaded_rf_model.predict(final_df)[0]

    # Display the prediction
    st.write(f"The predicted sales are: {prediction}.")

    # Save the input data to a CSV file
    input_df.to_csv("data.csv", index=False)

# Define custom CSS for the table
css = """
table {
    background-color: #f2f2f2;
    color: #333333;
}
"""
# Set custom CSS for the table
st.write(f'<style>{css}</style>', unsafe_allow_html=True)

# Add a download button for the CSV file
def download_csv():
    with open("data.csv", "r") as f:
        csv = f.read()
    b64 = base64.b64encode(csv.encode()).decode()
    button = f'<button class="download-button"><a href="data:file/csv;base64,{b64}" download="data.csv">Download Data CSV</a></button>'
    return button

st.markdown(f'<div style="text-align: center">{download_csv()}</div>', unsafe_allow_html=True)