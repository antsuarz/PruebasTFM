from feat import Detector 
import matplotlib.pyplot as plt

detector = Detector()

emotion = input("Introduzca el nombre de una emoción: ")
img_path = [f"./img/{emotion}.jpg"]
fex_result = detector.detect_image(img_path)

action_units = fex_result.aus
 
print(action_units)
print(fex_result.emotions)

csv_path = f"./csv_outputs/{emotion}_output.csv"
action_units.to_csv(csv_path, index=False)

figs = fex_result.plot_detections(poses=True)

image_path = f"./outputs/{emotion}_detections.png"
plt.savefig(image_path, bbox_inches='tight')
