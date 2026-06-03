# ✋ Air Writing — Gesture-Based Text Recognition

Write in the air using your index finger and let AI read what you wrote!  
Built with **OpenCV**, **MediaPipe**, and **Tesseract OCR**.

---

## 💡 What It Does
- Detects your hand in real-time using your webcam
- Tracks your **index finger** as a pen to write on screen
- Automatically reads what you wrote using **OCR (Tesseract)**
- Supports gesture controls:
  - ☝️ **One finger** → Draw / Write
  - ✌️ **Two fingers** → Select / Clear canvas

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Google-orange)
![Tesseract](https://img.shields.io/badge/OCR-Tesseract-red)

- **OpenCV** — real-time video capture and drawing
- **MediaPipe** — hand landmark detection
- **Tesseract OCR** — converting handwritten strokes to text
- **NumPy** — canvas and image processing

---

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/air-writing
cd air-writing
```

### 2. Install dependencies
```bash
pip install opencv-python mediapipe numpy pytesseract
```

### 3. Install Tesseract OCR
- Download from: https://github.com/UB-Mannheim/tesseract/wiki
- Install and note the path (default: `C:\Program Files\Tesseract-OCR\tesseract.exe`)
- Update line 7 in `main.py` if your path is different

### 4. Run
```bash
python main.py
```

---

## 🖐️ Gesture Guide
| Gesture | Action |
|---|---|
| Index finger only | Draw on canvas |
| Index + Middle finger | Enter selection mode |
| Point to CLEAR zone | Wipe canvas |

---

## 📌 Known Limitations
- Works best with **capital letters** in good lighting
- OCR accuracy depends on how clearly you write in the air
- Currently supports **A-Z only**

---

## 🔮 Future Improvements
- [ ] Add number recognition
- [ ] Word prediction using NLP
- [ ] Save written text to file
- [ ] Support for multiple colors

---

## 👩‍💻 Author
**Aparna Senthil**  
B.Tech CSE-AIDS | Vel Tech University  
📧 senthilaparna2006@gmail.com  
