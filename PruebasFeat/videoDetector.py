from feat import Detector
import matplotlib.pyplot as plt

detector = Detector()
emotion = input("Introduzca el nombre de una emoción: ")
video_path = f"./video/{emotion}.mp4"

video_prediction = detector.detect_video(video_path, skip_frames=30)
video_prediction.head()

print(video_prediction.shape)
video_prediction.emotions.plot()
save_video_path = f"./outputs/{emotion}_video_emotion_detections.png"
plt.savefig(save_video_path, bbox_inches='tight')
video_prediction.loc[[120, 1200]].plot_detections(faceboxes=False, add_titles=False)
save_video_path = f"./outputs/{emotion}_video_detections.png"
plt.savefig(save_video_path, bbox_inches='tight')
