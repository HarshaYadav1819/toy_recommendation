import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit app title
st.title("Toy Recommendation System")

# Direct file path
csv_path = "toy_recommendation_dataset.csv"

# Cached function to load data
@st.cache_data
def load_data(path):
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        return None

# Load data
data = load_data(csv_path)

if data is not None:
    st.success("File loaded successfully from the specified path!")

    # Display dataset preview
    st.write("### Dataset Preview:")
    st.dataframe(data.head())

    # Age selection dropdown
    unique_ages = sorted(data["age_suitability"].unique())
    selected_age = st.selectbox("Select Age Suitability:", unique_ages)

    if st.button("Show Toys for Selected Age"):
        age_filtered = data[data["age_suitability"] == selected_age]
        st.write(f"### Toys Suitable for Age {selected_age}:")
        st.dataframe(age_filtered[["toy_name", "price", "price_category", "rating"]])
else:
    st.error(f"File not found at {csv_path}. Please check the path.")
