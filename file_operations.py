from tkinter import filedialog, messagebox
from image_processing import save_image, display_image
from video_processing import save_video_with_audio
import os

def open_files(app):
    app.file_paths = filedialog.askopenfilenames(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg"), ("Video Files", "*.mp4;*.avi;*.mov")]
    )
    if app.file_paths:
        file_path = app.file_paths[0]
        if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
            display_image(app, file_path)
        elif file_path.lower().endswith((".mp4", ".avi", ".mov")):
            # Code to handle video preview can be added here
            pass

def save_files(app):
    if not app.resolution_combobox.get():
        messagebox.showinfo("Information", "Bitte wählen Sie eine Auflösung aus der Liste aus.")
        return

    if not app.filter_combobox.get():
        messagebox.showinfo("Information", "Bitte wählen Sie einen Filter aus der Liste aus.")
        return

    if not app.format_combobox.get():
        messagebox.showinfo("Information", "Bitte wählen Sie ein Format aus der Liste aus.")
        return

    resolution = app.resolution_combobox.get()
    width, height = map(int, resolution.split("x"))

    filter_selected = app.filter_combobox.get()
    format_selected = app.format_combobox.get()

    base_filename = app.filename_entry.get()
    if not base_filename:
        messagebox.showinfo("Information", "Bitte geben Sie einen Dateinamen ein.")
        return

    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        return

    for i, file_path in enumerate(app.file_paths, start=1):
        new_filename = f"{base_filename}{i}"
        new_file_path = os.path.join(folder_selected, new_filename + '.' + format_selected.lower())
        if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
            save_image(app, file_path, new_file_path, width, height, filter_selected, format_selected)
            display_image(app, new_file_path, width, height)
        elif file_path.lower().endswith((".mp4", ".avi", ".mov")):
            save_video_with_audio(file_path, new_file_path, width, height, filter_selected)
            # You can add code to update the video preview here
