from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Initialize the model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# ### Evaluate the model ###
# score = model.score(X_test, y_test)
# print(f"Accuracy : {score}")

# # Confusion matrix
# y_pred = model.predict(X_test)
# from sklearn.metrics import confusion_matrix

# confusion = confusion_matrix(y_test, y_pred)
# print(f"Confusion matrix : \n{confusion}")

# Export the model as a joblib file in the current directory
joblib.dump(model, "model.joblib")
