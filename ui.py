import tkinter as tk
from tkinter import ttk
import json

def initialize_ui(app):
    app.btn_open = tk.Button(app.root, text="Bilder/Videos auswählen", command=app.open_files)
    app.btn_open.pack()

    app.filename_entry = tk.Entry(app.root)
    app.filename_entry.pack()

    app.author_label = tk.Label(app.root, text="Autor")
    app.author_label.pack()
    app.author_entry = tk.Entry(app.root)
    app.author_entry.pack()

    app.copyright_label = tk.Label(app.root, text="Copyright")
    app.copyright_label.pack()
    app.copyright_entry = tk.Entry(app.root)
    app.copyright_entry.pack()

    app.software_label = tk.Label(app.root, text="Software")
    app.software_label.pack()
    app.software_entry = tk.Entry(app.root)
    app.software_entry.pack()

    initialize_comboboxes(app)
    app.btn_save = tk.Button(app.root, text="Speichern", command=app.save_files)
    app.btn_save.pack()

    app.picture_box = tk.Label(app.root)
    app.picture_box.pack(fill=tk.BOTH, expand=True)

def initialize_comboboxes(app):
    resolutions = ["32x32", "64x64", "128x128", "256x256", "320x320", "640x640", "720x720", 
                   "1080x1080", "1920x1920", "2048x2048", "3840x3840", "426x240", "640x360", 
                   "854x480", "1280x720", "1920x1080", "2560x1440", "3840x2160"]
    app.resolution_combobox = ttk.Combobox(app.root, values=resolutions, state="readonly")
    app.resolution_combobox.pack()

    filters = ["Kein Filter", "Schwarz-Weiß", "Sepia"]
    app.filter_combobox = ttk.Combobox(app.root, values=filters, state="readonly")
    app.filter_combobox.pack()

    formats = ["JPEG", "PNG", "ICO", "BMP", "GIF", "TIFF"]
    app.format_combobox = ttk.Combobox(app.root, values=formats, state="readonly")
    app.format_combobox.pack()

def load_design(app, design_file: str):
    with open(design_file, "r") as f:
        design = json.load(f)
    apply_design(app, design)

def apply_design(app, design: dict):
    for key, value in design.items():
        if key == "bg":
            app.root.configure(background=value)
        elif key in ["picture_box", "btn_open", "btn_save"]:
            getattr(app, key).configure(background=value)
        elif key == "btn_save_font":
            app.btn_save.configure(font=(value, 12))
        elif key == "filename_entry_bg":
            app.filename_entry.configure(background=value)
        elif key == "filename_entry_fg":
            app.filename_entry.configure(foreground=value)
