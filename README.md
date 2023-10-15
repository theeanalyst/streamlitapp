# Sales Prediction Web App with Streamlit

This is a Sales Prediction Web App built with Streamlit, a Python framework for creating interactive web applications. The app uses a pre-trained machine learning model to predict sales based on user-provided input parameters. In this README, we'll walk you through how to run the app and use it effectively.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Collecting User Input](#collecting-user-input)
- [Making Predictions](#making-predictions)
- [Custom Styling and Data Download](#custom-styling-and-data-download)
- [Running the App](#running-the-app)

## Prerequisites

Before running the Sales Prediction Web App, you'll need to have the following prerequisites installed on your system:

1. **Python**: Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Streamlit**: Install Streamlit using pip, the Python package manager:

   ```bash
   pip install streamlit
   ```

## Getting Started

To run the Sales Prediction Web App, follow these steps:

1. **Clone the Repository**: First, clone the repository to your local machine:
2. **Navigate to the App Directory**: Use the `cd` command to navigate to the directory where the app is located:

   ```bash
   cd sales-prediction-app
   ```

3. **Run the App**: Start the Streamlit app by running the following command:

   ```bash
   streamlit run app.py
   ```

   You'll see a local web server start, and the app will open in your default web browser.

## Collecting User Input

The Sales Prediction Web App provides an intuitive interface for users to input data. Users can provide both categorical and numerical data to make sales predictions. The input fields include:

- Product Category
- State
- Store Type
- End of the Month Indicator
- Store Number
- On Promotion Indicator
- Cluster
- Oil Price
- Year
- Month
- Day of the Month
- Day of the Week

Users can choose product categories, states, and store types from dropdown menus. They can also indicate whether it's the end of the month using a radio button. Numerical input fields are controlled with sliders or number input fields.

## Making Predictions

Once users have provided their input, they can click the "Predict" button to obtain sales predictions. The app performs the following steps:

1. **Data Collection**: User-provided data is collected and organized into a pandas DataFrame.

2. **Data Preprocessing**: The app applies data preprocessing steps, including encoding categorical variables and scaling numerical features using the pre-trained machine learning toolkit.

3. **Sales Prediction**: The input data is fed into a pre-trained Random Forest model, and a sales prediction is generated.

4. **Result Display**: The app displays the predicted sales to the user.

## Custom Styling and Data Download

The Sales Prediction Web App comes with custom styling to make the displayed data visually appealing. We've applied custom CSS to the table to enhance its appearance. Additionally, users can download their input data for further analysis.

## Running the App

To use the app, follow the steps outlined in the "Getting Started" section to run the Streamlit app. Once the app is running, you can:

- Input your data in the provided fields.
- Click the "Predict" button to get a sales prediction.
- Download your input data in CSV format using the provided button.

This Sales Prediction Web App simplifies the process of making sales predictions and is a valuable tool for businesses looking to optimize their operations. Enjoy using the app!
