# main.py
import tensorflow as tf
import numpy as np
from PIL import Image

# Chargement du modèle
model = tf.keras.models.load_model("model/cnnclassificator.h5")

# Prédiction pour une image donnée
def predict(image_path):
    img = Image.open(image_path)
    img = img.resize((256, 256))
    img = np.array(img) / 255.0
    prediction = model.predict(np.expand_dims(img, 0))

    return prediction[0]

# Exemple d'utilisation
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = "image.jpg"
    prediction = predict(image_path)
    print("Prédiction pour l'image {}: {}".format(image_path, prediction))
