from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import joblib

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Initialiser 3 modèles différents
models = {"rf": RandomForestClassifier(), "svm": SVC(), "knn": KNeighborsClassifier()}

# Entraîner les 3 modèles et sauvegarder les fichiers joblib
for name, model in models.items():
    model.fit(X_train, y_train)
    joblib.dump(model, f"server/{name}.joblib")

# Evaluer les modèles
# score = {name: model.score(X_test, y_test) for name, model in models.items()}
# print(f"Accuracy : {score}")

# y_preds = {name: model.predict(X_test) for name, model in models.items()}
# confusion = {name: confusion_matrix(y_test, y_preds[name]) for name in models.keys()}
# print(f"Confusion matrix : \n{confusion}")
