# Importar la biblioteca OpenCV
import cv2
#Importar las funciones LeerEleccion, Cachipun y Arbitraje
from functions import LeerEleccion, Cachipun, Arbitraje

# Abrir la cámara predeterminada (índice 0), si incluyes otras como una webcam externa puedes cambiarlo a (1)
cap = cv2.VideoCapture(0)

# Establecer el ancho del fotograma en 640 píxeles
cap.set(3, 1920)

# Establecer la altura del fotograma en 480 píxeles
cap.set(4, 1080)

c = 1

# Bucle infinito para capturar continuamente fotogramas de la cámara
while True:
    # Leer un fotograma de la cámara
    ret, img = cap.read()

    # Mostrar el fotograma capturado en una ventana llamada "Cam"
    cv2.imshow('Cam', img)

    if ret == True:
        if cv2.waitKey(1)==ord('s'):
            name = "foto"+str(c)+".png"
            cv2.imwrite(name, img)

            player, _ = LeerEleccion(name)
            print("Creo que tu eleccion es", player)

            # Randint for machine
            machine = Cachipun(player)
            print("Asi que mi eleccion es", machine, "\n")

            print(Arbitraje(player, machine))

            c += 1
        elif cv2.waitKey(1) == ord('q'):
            break
    else:
	    print("Error al acceder a la cámara")

# Liberar la cámara
cap.release()

# Cerrar todas las ventanas de OpenCV
cv2.destroyAllWindows()