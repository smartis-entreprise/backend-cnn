# Backend for model-cnn

## Prerequisite

- [Docker](https://www.docker.com/)

Test if docker is correctly installed:

```bash
docker -v
```

## Running container

```bash
# clone repo
git clone git@github.com:smartis-entreprise/backend-cnn.git
cd backend-cnn

# build and verify
sudo docker build -t backend-cnn .
sudo docker images

# run the image
sudo docker run -p 5000:5000 backend-cnn
```
