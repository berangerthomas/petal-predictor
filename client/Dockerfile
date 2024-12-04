FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app 

RUN pip install -r requirements.txt

COPY app.py app.py
COPY images/iris_setosa.jpg images/iris_setosa.jpg
COPY images/iris_versicolor.jpg images/iris_versicolor.jpg
COPY images/iris_virginica.jpg images/iris_virginica.jpg

CMD ["streamlit", "run", "app.py"]
