from deepface import DeepFace
import cv2

def detectar_emocion(imagen_path): 
    
    img = cv2.imread(imagen_path)
    try:
        
        resultado = DeepFace.analyze(img, actions=['emotion'])
        emocion_dominante = resultado[0]['dominant_emotion']
        
        print(f"La emoción detectada es {emocion_dominante}.")
    
    except Exception as e:
        print(f"Ha ocurrido un error al analizar la imagen: {e}")
