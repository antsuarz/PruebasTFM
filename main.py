from piloto1 import detectar_emocion
from piloto2 import detectar_emociones

if __name__ == "__main__":
    
    
    while True:
        emocion = input("Introduzca el nombre de una emoción: ")
        imagen_path = f"./img/{emocion}.jpg" 
    
        # detectar_emocion(imagen_path)
        detectar_emociones(imagen_path)