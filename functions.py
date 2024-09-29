from keras.models import load_model  # TensorFlow es requerido para que Keras funcione
from PIL import Image, ImageOps  # Recordar instalar pillow, no PIL
import numpy as np
import random

def LeerEleccion(RutaImagen):
    # Desactivar notacion cientifica para mayor claridad
    np.set_printoptions(suppress=True)

    # Cargar el modelo
    model = load_model("IA\keras_model.h5", compile=False)

    # Cargar los labels
    class_names = open("IA\labels.txt", "r").readlines()

    # Crea el array de la forma correcta para alimentar el modelo de keras
    # El 'lenght' o cantidad de imagenes que se pueden poner en el array
    # es determinado por la 1ra posicion en la tupla 'shape' (en este caso 1)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Buscamos la imagen en la ruta especificada
    image = Image.open(RutaImagen).convert("RGB")

    # Redimensionamos la imagen a 224x224 y la cortamos, quedandonos con el centro
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Transforma la imagen a un numpy array
    image_array = np.asarray(image)

    # Normalizamos la imagen
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Carga la imagen al array
    data[0] = normalized_image_array

    # Hacemos una prediccion con el modelo
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print de la prediccion y la seguridad de esta
    #print("Clase:", class_name[2:], end="")
    #print("Seguridad:", confidence_score)

    return class_name[2:], confidence_score

# Un algoritmo de cachipun Imposible de Ganar
def CachipunImposible(eleccion):
    if eleccion == "Piedra\n":
        return 'Papel'
    elif eleccion == "Papel\n":
        return 'Tijera'
    elif eleccion == "Tijera\n":
        return 'Piedra'
    else:
        raise 'No pude reconocer tu eleccion'

# Un algoritmo de cachipun con elección aleatoria por parte de la máquina
def CachipunAleatorio(eleccion):
    if eleccion == "Piedra\n" or eleccion == "Papel\n" or eleccion == "Tijera\n":
        return random.choice(['Piedra', 'Papel', 'Tijera'])
    else:
        raise 'No pude reconocer tu eleccion'

# Un algoritmo de arbitraje justo, en la practica nunca sera usado en
def Arbitraje(jugador, maquina):
    maquina = maquina+'\n'
    if jugador == maquina:
        return "Empate"
    
    elif (jugador == 'Piedra\n' and maquina == 'Tijera\n') or (jugador == 'Tijera\n' and maquina == 'Papel\n') or (jugador == 'Papel\n' and maquina == 'Piedra\n'):
        return "Ganaste, Felicidades Jugador!!!"

    else:
        return "Vuelvo a ganar!!! Suerte la próxima vez"
