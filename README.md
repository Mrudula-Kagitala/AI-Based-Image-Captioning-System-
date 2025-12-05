📌 AI-Based Image Captioning System

This project is a web-based application that automatically generates captions for uploaded images using a Vision-Language Transformer model (BLIP).
It also supports multilingual translation and text-to-speech output, making it accessible for visually impaired and non-English users.

🚀 Features

✔ Upload an image and generate an automatic caption
✔ Uses BLIP transformer model for accurate captioning
✔ Translate captions into multiple languages
✔ Listen to the caption using text-to-speech
✔ Simple, responsive web interface

🧠 Tech Stack

Programming Language -- Python
Backend Framework -- Flask
AI Model -- BLIP (Hugging Face Transformers)
Deep Learning Library -- PyTorch
Text-to-Speech -- gTTS
Translation -- deep-translator
UI -- HTML, CSS, JavaScript

📁 Project Structure

AI-Image-Captioning-System/
│
├─ app.py
├─ requirements.txt
├─ README.md
│
├─ templates/
│   └─ index.html
│
└─ static/
    ├─ style.css
    └─ script.js

▶️ How to Run the Project

1️⃣ Clone the Repository
https://github.com/Mrudula-Kagitala/AI-Based-Image-Captioning-System-.git

cd AI-Image-Captioning-System

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run the Application
python app.py

6️⃣ Open in Browser
http://127.0.0.1:5000

🖼 Sample Output

Input Image	Generated Caption
🐶 Dog Image	"A dog sitting on the grass"
🚲 Bicycle Image	"A bicycle parked on a street"


<img width="1837" height="933" alt="Screenshot 2025-12-05 133434" src="https://github.com/user-attachments/assets/1a9f7f64-7dcd-4ee5-a2f1-e61c2b18d5d8" />


<img width="908" height="885" alt="Screenshot 2025-12-05 133655" src="https://github.com/user-attachments/assets/8c5fcf8d-43ee-4c1a-a61f-f160e724c825" />


<img width="758" height="898" alt="Screenshot 2025-12-05 134217" src="https://github.com/user-attachments/assets/a4d5ac7b-483f-49a3-b548-645d89cd6508" />


📚 How It Works

The user uploads an image from the browser.

The Flask backend receives the file via REST POST API.

The BLIP model processes the image and generates a caption.

If selected, the caption is translated using deep-translator.

The caption is converted to audio using gTTS and sent back to the frontend.

The user can view the text and listen to the spoken caption.

🛠 Future Enhancements

🔹 Deploy to cloud with GPU support
🔹 Add offline translation and offline TTS
🔹 Improve UI with drag-and-drop image upload
🔹 Store user history using a database
