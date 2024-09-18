from deepface import DeepFace
import cv2

def detectar_emociones(imagen_path): 
    
    img = cv2.imread(imagen_path)
    try:
        
        result = DeepFace.analyze(img, actions=['emotion'])
        dominant_emotion = result[0]['dominant_emotion']
        emotion = result[0]['emotion'] 
        
        print("\033[93m" + "-----------------------------------------------" + "\033[0m")
        for emotion, porcentaje in emotion.items():
            print(f"{emotion}: {porcentaje:.2f}%")
        print("\033[93m" + "-----------------------------------------------" + "\033[0m")
        
        print("\033[92m" + f"Dominant emotion: {dominant_emotion}." + "\033[0m")
    
    except Exception as e:
        print("\033[91m" + f"ERROR: {e}" + "\033[0m")
