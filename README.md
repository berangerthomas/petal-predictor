# ⚡⚡⚡ Petal predictor™ ⚡⚡⚡

Le futur de l'horticulture.

Vous ne vendez que des iris ? Ce service est fait pour vous. Mesurer les caractéristiques de vos specimens d'iridaceae, et notre intelligence artificielle prédira leur espèce avec une précision qui ferait pâlir un botaniste !

Iris setosa, versicolor ou virginica ? Plus fiable qu'un jardinier à la retraite, Petal predictor™ vous donnera la réponse en un instant !

Petal predictor™, la puissance de l'IA au service des plantes.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé Docker et Docker Compose sur votre machine.

## Cloner le projet

Pour cloner ce projet, exécutez la commande suivante dans votre terminal :

```bash
git clone https://github.com/berangerthomas/petal-predictor
```

## Lancer le projet

Ensuite, accédez au répertoire racine du projet et démarrer les services en exécutant la commande suivante :

```bash
docker-compose up --build
```

Cette commande construira les images Docker nécessaires et démarrera les services définis dans le fichier `docker-compose.yml`.

## Accéder aux services

- **Client (Streamlit)** : Accédez à `http://localhost:8501`
- **Serveur API (FastAPI)** : Accédez à `http://localhost:8000`

## Arrêter les services

Pour arrêter les services, appuyez sur `Ctrl+C` dans le terminal où les services sont en cours d'exécution, puis exécutez :

```bash
docker-compose down
```

Cela arrêtera et supprimera les conteneurs créés par `docker-compose up`.
