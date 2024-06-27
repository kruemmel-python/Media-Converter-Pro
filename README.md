# MediaConverterPro

MediaConverterPro ist ein vielseitiges Tool zur Stapelverarbeitung von Bildern und Videos. Es ermöglicht das Konvertieren, Anwenden von Filtern und Hinzufügen von Metadaten zu Bildern und Videos in verschiedenen Formaten.

## Inhaltsverzeichnis

- [Features](#features)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Dateistruktur](#dateistruktur)
- [Abhängigkeiten](#abhängigkeiten)
- [Offizielle Dokumentationen](#offizielle-dokumentationen)
- [Contributing](#contributing)
- [Lizenz](#lizenz)

## Features

- Unterstützt verschiedene Bildformate: JPEG, PNG, ICO, BMP, GIF, TIFF
- Unterstützt verschiedene Videoformate: MP4, AVI, MOV
- Anwenden von Filtern (Schwarz-Weiß, Sepia) auf Bilder und Videos
- Hinzufügen von Exif-Daten zu Bildern
- Einfache Benutzeroberfläche zur Auswahl von Dateien und Einstellungen

## Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/DeinBenutzername/MediaConverterPro.git
   cd MediaConverterPro
   ```

2. **Virtuelle Umgebung erstellen:**
   ```bash
   python -m venv venv
   source venv/bin/activate # für Linux/Mac
   venv\Scripts\activate # für Windows
   ```

3. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

1. **Starten der Anwendung:**
   ```bash
   python app.py
   ```

2. **Bedienung:**
   - Klicken Sie auf "Bilder/Videos auswählen", um die zu verarbeitenden Dateien auszuwählen.
   - Geben Sie den Dateinamen, Autor, Copyright und Software in die entsprechenden Felder ein.
   - Wählen Sie die gewünschte Auflösung und das Ausgabeformat aus den Dropdown-Menüs.
   - Wählen Sie einen Filter aus, falls gewünscht.
   - Klicken Sie auf "Speichern", um die Dateien zu konvertieren und zu speichern.

## Dateistruktur

```
MediaConverterPro/
├── app.py
├── design.json
├── file_operations.py
├── image_processing.py
├── requirements.txt
├── ui.py
└── video_processing.py
```

- **app.py**: Hauptanwendung, die die Benutzeroberfläche und die Hauptlogik enthält.
- **design.json**: Datei für Design-Parameter der Benutzeroberfläche.
- **file_operations.py**: Modul für Dateioperationen wie das Öffnen und Speichern von Dateien.
- **image_processing.py**: Modul für Bildverarbeitungsfunktionen.
- **ui.py**: Modul für die Initialisierung der Benutzeroberfläche.
- **video_processing.py**: Modul für Videobearbeitungsfunktionen.
- **requirements.txt**: Liste der Abhängigkeiten für das Projekt.

## Abhängigkeiten

- [Tkinter](https://docs.python.org/3/library/tkinter.html): Bibliothek für die Erstellung von GUIs in Python.
- [Pillow](https://pillow.readthedocs.io/en/stable/): Bibliothek für Bildverarbeitung in Python.
- [OpenCV](https://docs.opencv.org/master/): Bibliothek für die Verarbeitung von Videos und Bildern.
- [ffmpeg-python](https://github.com/kkroening/ffmpeg-python): Python-Bindings für FFmpeg.
- [Piexif](https://piexif.readthedocs.io/en/latest/): Bibliothek zum Bearbeiten von Exif-Daten in Bildern.

## Offizielle Dokumentationen

- [Tkinter Dokumentation](https://docs.python.org/3/library/tkinter.html)
- [Pillow Dokumentation](https://pillow.readthedocs.io/en/stable/)
- [OpenCV Dokumentation](https://docs.opencv.org/master/)
- [ffmpeg-python Dokumentation](https://github.com/kkroening/ffmpeg-python)
- [Piexif Dokumentation](https://piexif.readthedocs.io/en/latest/)

## Contributing

Beiträge sind herzlich willkommen! Bitte öffnen Sie ein Issue, um Fehler zu melden oder Funktionen anzufordern. Pull-Requests sind ebenfalls willkommen.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.

