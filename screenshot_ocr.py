#!/usr/bin/env python3

import tempfile
import subprocess
from PIL import Image
from pytesseract import image_to_string
import pyperclip

def capture_screenshot(file_path):
    subprocess.run(['gnome-screenshot', '-a', '-f', file_path],
                   stderr=subprocess.DEVNULL)


def extract_text_from_image(file_path):
    with Image.open(file_path) as image:
        image = image.resize((image.width * 2, image.height * 2), Image.BICUBIC)
        text = image_to_string(image, lang="eng")
    return text

def main():
    with tempfile.NamedTemporaryFile(suffix=".png") as tmp_file:
        capture_screenshot(tmp_file.name)
        extracted_text = extract_text_from_image(tmp_file.name)
        pyperclip.copy(extracted_text)

if __name__ == "__main__":
    main()

   

