import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset 
data = pd.read_csv("C:/Users/HINAL/OneDrive/Documents/Custom Office Templates/housing_price_dataset.csv")

data_cleaned = data.dropna()


# Sidebar filters
min_square_feet = st.sidebar.slider('Minimum Square Feet', min_value=data['SquareFeet'].min(), max_value=data['SquareFeet'].max())
max_price = st.sidebar.slider('Maximum Price', min_value=data['Price'].min(), max_value=data['Price'].max())

# Filter data based on user input
filtered_data = data[(data['SquareFeet'] >= min_square_feet) & (data['Price'] <= max_price)]

# Display basic information about the dataset
st.write("## Data Summary")
st.table(filtered_data.describe())

# Scatter plot
st.write("## Scatter Plot")
scatter_fig = px.scatter(filtered_data, x='SquareFeet', y='Price', hover_data=['Bedrooms', 'Bathrooms'], title='Square Feet vs Price')
st.plotly_chart(scatter_fig)

# Histograms
st.write("## Histograms")
hist_fig = px.histogram(filtered_data, x=['SquareFeet', 'Bedrooms', 'Bathrooms', 'Price'], marginal='box')
st.plotly_chart(hist_fig)

