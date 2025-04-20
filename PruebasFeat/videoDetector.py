from feat import Detector
import matplotlib.pyplot as plt

frames_to_skip = 30.0

def detect_video(video_path, skip_frames):
    detector = Detector()
    return detector.detect_video(video_path, skip_frames=skip_frames)


def plot_action_units_mean(video_prediction, video_id):
    action_units = video_prediction.filter(like="AU")
    mean_action_units = action_units.mean()

    plt.figure(figsize=(10, 5))
    mean_action_units.plot(kind='bar', color='blue')
    plt.title("Mean of Action Units")
    plt.xlabel("Action Units")
    plt.ylabel("Mean Value")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(f"./outputs/{video_id}_mean_au_plot.png", bbox_inches='tight')
    plt.show()

def main():
    video_id = input("Video a analizar: ")
    video_path = f"./video/{video_id}.mp4"

    print(video_path)
    prediction = detect_video(video_path, frames_to_skip)
    print(prediction.shape)

    plot_action_units_mean(prediction, video_id)


if __name__ == "__main__":
    main()
