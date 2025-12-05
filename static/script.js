const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const resultBox = document.getElementById("result");
let audioBase64 = null;

// Preview Image
imageInput.addEventListener("change", () => {
    const file = imageInput.files[0];
    if (file) {
        previewImage.src = URL.createObjectURL(file);
        previewImage.style.display = "block";
    }
});

// Submit Form
document.getElementById("uploadForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append("image", imageInput.files[0]);
    formData.append("language", document.getElementById("language").value);

    const response = await fetch("/generate_caption", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("captionText").innerText = data.caption;
    audioBase64 = data.audio;

    resultBox.style.display = "block";
});

function playAudio() {
    if (audioBase64) {
        const audio = new Audio(`data:audio/mp3;base64,${audioBase64}`);
        audio.play();
    }
}
