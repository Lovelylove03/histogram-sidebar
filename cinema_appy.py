
import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
# Load the dataset
link = "https://raw.githubusercontent.com/Lovelylove03/histogram-sidebar/main/df_ml%20-%20df_ml.csv"
df = pd.read_csv(link)


# Ensure the dataframe has been loaded correctly
st.write(df.head())

# Sidebar for histogram options
st.sidebar.header("Histogram Options")

# Sidebar options for year range selection
min_year = int(df['startYear'].min())
max_year = int(df['startYear'].max())
year_range = st.sidebar.slider('Select year range', min_year, max_year, (min_year, max_year))

# Filter the dataset based on the selected year range
df_filtered = df[(df['startYear'] >= year_range[0]) & (df['startYear'] <= year_range[1])]

# Check if 'startYear' is in the columns
if 'startYear' in df.columns:
    # Convert 'startYear' to numeric, forcing errors to NaN
    df_filtered['startYear'] = pd.to_numeric(df_filtered['startYear'], errors='coerce')

    # Drop rows with NaN values in 'startYear'
    df_filtered = df_filtered.dropna(subset=['startYear'])

    # Sidebar option for number of bins in the histogram
    bins = st.sidebar.slider('Number of bins', 10, 100, 30)

    # Plot the histogram
    fig, ax = plt.subplots()
    df_filtered['startYear'].plot(kind='hist', bins=bins, ax=ax, edgecolor='black')
    ax.set_title('Histogram of Start Year')
    ax.set_xlabel('Start Year')
    ax.set_ylabel('Frequency')

    # Display the plot in Streamlit
    st.pyplot(fig)
else:
    st.write("The dataset does not contain a 'startYear' column.")
