from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Charger le jeu de données Iris
iris = load_iris()
X, y = iris.data, iris.target

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Initialiser le modèle
model = RandomForestClassifier()

# Entraîner le modèle
model.fit(X_train, y_train)

# ### Évaluer le modèle ###
# score = model.score(X_test, y_test)
# print(f"Précision : {score}")

# # Matrice de confusion
# y_pred = model.predict(X_test)
# from sklearn.metrics import confusion_matrix

# confusion = confusion_matrix(y_test, y_pred)
# print(f"Matrice de confusion : \n{confusion}")

# Exporter le modele en joblib dans le répertoire courant
joblib.dump(model, "model.joblib")
