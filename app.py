import tkinter as tk
from ui import initialize_ui, load_design
from file_operations import open_files, save_files

class App:
    def __init__(self, root: tk.Tk, design_file: str):
        self.root = root
        self.file_paths = []
        initialize_ui(self)
        load_design(self, design_file)

    def open_files(self):
        open_files(self)

    def save_files(self):
        save_files(self)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root, "design.json")
    root.mainloop()
