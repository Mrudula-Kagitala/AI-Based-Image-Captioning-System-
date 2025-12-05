import os
from flask import Flask, render_template, request, jsonify
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from gtts import gTTS
from deep_translator import GoogleTranslator
from io import BytesIO
import base64
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load BLIP Model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to(device)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_caption", methods=["POST"])
def generate_caption():
    image = request.files["image"]
    lang = request.form.get("language", "en")

    img = Image.open(image).convert("RGB")

    inputs = processor(images=img, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_length=50)

    caption = processor.decode(output[0], skip_special_tokens=True)

    # Translate caption if needed
    if lang != "en":
        caption = GoogleTranslator(source="auto", target=lang).translate(caption)

    # Convert to Audio
    tts = gTTS(caption, lang=lang)
    buffer = BytesIO()
    tts.write_to_fp(buffer)
    audio_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return jsonify({"caption": caption, "audio": audio_base64})

if __name__ == "__main__":
    app.run(debug=True)
