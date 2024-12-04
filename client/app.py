import streamlit as st
import requests


# Function to get the list of fruits from the server
def get_prediction(json_data):
    url = "http://server:8000/predict"
    try:
        response = requests.post(url, json=json_data)
        if response.status_code == 200:
            prediction = response.json()
            return prediction
        else:
            return (
                f"Failed to fetch fruits. Server responded with: {response.status_code}"
            )
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}"


# Configuration de la largeur de la page
st.set_page_config(layout="wide")  # Ou wide pour prendre toute la largeur

# Titre
st.title("Prédiction de l'espèce Iris")

# infos sous le titre
st.write("Ajustez les curseurs pour modifier les caractéristiques de la fleur.")

# Créer deux colonnes
col1, col2 = st.columns([2, 1])

# Première colonne pour les curseurs
with col1:
    sepal_length = st.slider("Longueur du sépale", 4.0, 8.0, 5.8)
    sepal_width = st.slider("Largeur du sépale", 2.0, 4.5, 3.0)
    petal_length = st.slider("Longueur du pétale", 1.0, 7.0, 4.35)
    petal_width = st.slider("Largeur du pétale", 0.1, 2.5, 1.3)

    # Bouton pour effectuer la prédiction
    predict_button = st.button("Prédire")

# Deuxième colonne pour l'image
with col2:
    if predict_button:
        # Préparer les données d'entrée
        input_data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        }

        # Faire appel à l'API pour la prédiction
        prediction = get_prediction(input_data)

        # Récupération de l'identifiant de l'espèce prédite
        id_pred = prediction["prediction"]

        # Dictionnaire pour mapper les étiquettes aux espèces
        species = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}

        # Afficher le résultat
        st.write(f"L'espèce prédite est : **{species[id_pred]}**")

        # Dictionnaire pour mapper les espèces aux noms de fichiers d'images
        images = {
            0: "images/iris_setosa.jpg",
            1: "images/iris_versicolor.jpg",
            2: "images/iris_virginica.jpg",
        }

        # Afficher l'image correspondante
        st.image(images[id_pred], caption=f"{species[id_pred]}")
