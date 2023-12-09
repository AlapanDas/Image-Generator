import tkinter as tk
from tkinter import Entry, Button
import requests
import io
from PIL import Image, ImageTk

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
HEADERS = {"Authorization": "Bearer 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"}

root = tk.Tk()
root.title("Text to Image")


def generate_image():
    text_input = entry.get() 

    # Send a request to the Hugging Face API with the text input
    payload = {"inputs": text_input}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    image_bytes = response.content


    image = Image.open(io.BytesIO(image_bytes))
    tk_image = ImageTk.PhotoImage(image)
    image_label.config(image=tk_image)
    image_label.image = tk_image  
# Create a text input field
entry = Entry(root, width=50)
entry.pack(pady=30)

# Create a button to generate and display the image
generate_button = Button(root, text="Generate Image", command=generate_image)
generate_button.pack()

image_label = tk.Label(root)
image_label.pack()


root.mainloop()
