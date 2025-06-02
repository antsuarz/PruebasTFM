from feat import Detector
import matplotlib.pyplot as plt
import os

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

    mean_action_units.to_csv(f"./csv_outputs/{video_id}_mean_au.csv", index=True)
    plt.close()

def main():
    for file_name in os.listdir("./video"):
        if "-converted" in file_name and file_name.endswith(".mp4"):
            video_path = os.path.join("./video", file_name)

            print("-------------------------------------------")
            print(f"Video: {video_path}")
            video = detect_video(video_path, frames_to_skip)
            print(video.shape)

            plot_action_units_mean(video, file_name)
            print("-------------------------------------------")


if __name__ == "__main__":
    main()
