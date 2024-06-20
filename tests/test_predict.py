import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','app')))

#__file__ est une variable spéciale en Python qui contient le chemin du fichier script actuel.
#os.path.dirname(__file__) renvoie le répertoire contenant ce fichier script. Autrement dit, cela donne le chemin du répertoire où se trouve le fichier en cours d'exécution.
#os.path.join est une fonction qui combine des éléments de chemin en un seul chemin. Ici, elle combine le chemin du répertoire contenant le fichier script avec '..'.
#'..' est une notation pour le répertoire parent. Donc,
#os.path.join(os.path.dirname(__file__), '..') donne le chemin du répertoire parent du répertoire contenant le script actuel.
#os.path.abspath prend un chemin relatif et le convertit en chemin absolu. Cela assure que le chemin résultant est un chemin complet à partir de la racine du système de fichiers.
#sys.path est une liste en Python qui contient les chemins où le moteur d'importation de Python cherche des modules.
#append ajoute un élément à la fin de cette liste.
#En ajoutant le chemin absolu du répertoire parent à sys.path, vous permettez à Python de chercher des modules dans ce répertoire lorsque vous utilisez l'instruction import.

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_image():
    filepath = "tests/files/picture.jpg"
    response = client.post(
        "/predict", files={"file": ("filename", open(filepath, "rb"), "image/jpeg")}
    )
    assert response.status_code == 200

def test_predict_text():
    filepath = "tests/files/text.txt"
    response = client.post(
        "/predict", files={"file": ("filename", open(filepath, "rb"), "text/plain")}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "File provided is not an image."}
