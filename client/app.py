import streamlit as st
import requests


# Function to get the prediction
def get_prediction(json_data):
    url = "http://server:8000/predict"
    try:
        response = requests.post(url, json=json_data)
        if response.status_code == 200:
            prediction = response.json()
            return prediction
        else:
            return f"Impossible de récupérer la prédiction: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Erreur : {e}"


# Configure the page width
st.set_page_config(layout="wide")  # Or wide to take the full width

# Title
st.title("Iris Species Prediction using RF")

# Information below the title
st.write("Adjust the sliders to modify the flower's characteristics.")

# Create two columns
col1, col2 = st.columns([2, 1])

# Première colonne pour les curseurs
with col1:
    sepal_length = st.slider("Sepal length", 4.0, 8.0, 5.8)
    sepal_width = st.slider("Sepal width", 2.0, 4.5, 3.0)
    petal_length = st.slider("Petal length", 1.0, 7.0, 4.35)
    petal_width = st.slider("Petal width", 0.1, 2.5, 1.3)

    # Button to make the prediction
    predict_button = st.button("Predict")

# Second column for the image
with col2:
    if predict_button:
        # Prepare input data
        input_data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        }

        # Call the API for prediction
        prediction = get_prediction(input_data)

        # Retrieve the predicted species ID
        id_pred = prediction["prediction"]

        # Dictionary to map labels to species
        species = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}

        # Display the result
        st.write(f"The predicted species is: **{species[id_pred]}**")

        # Dictionary to map species to image file names
        images = {
            0: "images/iris_setosa.jpg",
            1: "images/iris_versicolor.jpg",
            2: "images/iris_virginica.jpg",
        }

        # Display the corresponding image
        st.image(images[id_pred], caption=f"{species[id_pred]}")
