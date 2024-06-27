import cv2
import ffmpeg
import os
import numpy as np
from PIL import Image, ImageOps

def save_video_with_audio(file_path: str, new_file_path: str, width: int, height: int, filter_selected: str):
    # Use OpenCV to process the video frames
    cap = cv2.VideoCapture(file_path)
    temp_video_path = "temp_video.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(temp_video_path, fourcc, 20.0, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (width, height))
        if filter_selected == "Schwarz-Weiß":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        elif filter_selected == "Sepia":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame = ImageOps.colorize(frame.convert("L"), "#FF962E", "#FF5E5E", "#FFFF33")
            frame = np.array(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        out.write(frame)

    cap.release()
    out.release()

    # Use ffmpeg to combine the processed video frames with the original audio
    input_video = ffmpeg.input(temp_video_path)
    input_audio = ffmpeg.input(file_path)
    ffmpeg.output(input_video, input_audio, new_file_path, vcodec='copy', acodec='aac', strict='experimental').run(overwrite_output=True)

    # Remove the temporary video file
    os.remove(temp_video_path)
