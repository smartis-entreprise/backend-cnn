# Backend for model-cnn

Ce backend est conçu pour héberger un modèle de réseau neuronal convolutionnel (CNN) pour la reconnaissance d'images. Il utilise Docker pour créer un environnement de déploiement isolé et utilisable.

## Prérequis

- [Docker](https://www.docker.com/)

Veuillez vous assurer que Docker est correctement installé en exécutant la commande suivante dans votre terminal:

```bash
docker -v
```

## Démarrage du conteneur

Pour démarrer le conteneur Docker associé à ce backend, veuillez suivre les étapes suivantes :

1. Clonez le dépôt Git:

```bash
git clone git@github.com:smartis-entreprise/backend-cnn.git
```

2. Accédez au répertoire cloné:

```bash
cd backend-cnn
```

3. Construisez l'image Docker:

```bash
sudo docker build -t backend-cnn .
```

Vous pouvez vérifier que l'image a été correctement construite en exécutant la commande suivante:

```bash
sudo docker images
```

4. Exécutez l'image:

```bash
sudo docker run -p 5000:5000 backend-cnn
```

Le backend devrait maintenant être accessible via l'adresse `http://localhost:5000`. Vous devriez obtenir une sortie similaire à celle-ci:

```bash
"Prédiction pour l'image image.jpg: [0.00019254]"
```