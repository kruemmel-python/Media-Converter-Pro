from PIL import Image, ImageOps, ImageTk
import piexif

def save_image(app, file_path: str, new_file_path: str, width: int, height: int, filter_selected: str, format_selected: str):
    image = Image.open(file_path)
    image = image.resize((width, height))

    if filter_selected == "Schwarz-Weiß":
        image = image.convert("L")
    elif filter_selected == "Sepia":
        image = ImageOps.colorize(image.convert("L"), "#3A200D", "#704214")

    if format_selected.upper() == "ICO":
        image = image.resize((64, 64), Image.LANCZOS)  # ICO format requires specific sizes

    exif_data = {
        "0th": {
            piexif.ImageIFD.Artist: app.author_entry.get(),
            piexif.ImageIFD.Copyright: app.copyright_entry.get(),
            piexif.ImageIFD.Software: app.software_entry.get(),
        }
    }

    exif_bytes = piexif.dump(exif_data)
    if format_selected.upper() in ["JPEG", "TIFF"]:
        image.save(new_file_path, format=format_selected, exif=exif_bytes)
    else:
        image.save(new_file_path, format=format_selected)

def display_image(app, file_path: str, original_width: int = None, original_height: int = None):
    image = Image.open(file_path)
    if original_width and original_height:
        preview_width = original_width // 5
        preview_height = original_height // 5
    else:
        preview_width, preview_height = image.size[0] // 5, image.size[1] // 5

    image = image.resize((preview_width, preview_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    app.picture_box.config(image=photo)
    app.picture_box.image = photo
