import tensorflow as tf
import numpy as np
from PIL import Image

# Chargement du modèle
model = tf.keras.models.load_model("cnnclassificator.h5")

# Prédiction pour une image donnée
def predict(image_path):
    # Chargement de l'image et prétraitement
    image = Image.open(image_path)
    image = image.resize((32, 32))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Prédiction du modèle
    prediction = model.predict(image)
    prediction = np.argmax(prediction, axis=1)

    return prediction[0]

# Exemple d'utilisation
if __name__ == "__main__":
    image_path = "image.jpg"
    prediction = predict(image_path)
    print("Prédiction pour l'image {}: {}".format(image_path, prediction))
