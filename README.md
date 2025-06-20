# ✋ Finger Counter Using Hand Gesture

A real-time computer vision project that uses your webcam to count how many fingers you are holding up! Built with Python, OpenCV, and MediaPipe, this project accurately tracks your hand and identifies raised fingers using landmark detection — ideal for gesture-based applications and human-computer interaction.

---

## 🧠 Overview

This project demonstrates how computer vision and machine learning can be used to interact with machines without traditional input devices. By detecting hand landmarks and analyzing finger positions, the system determines the number of fingers being held up in real time.

It’s a beginner-friendly yet powerful demonstration of:

- Hand detection using MediaPipe
- Custom landmark tracking and logic
- Real-time feedback through OpenCV visuals

---

## 📌 Features

✅ Real-time hand detection via webcam  
✅ Counts raised fingers (0 to 5) with high accuracy  
✅ Clean visual overlay showing hand landmarks and count  
✅ Modular code with a reusable `HandTrackingModule`  
✅ Lightweight and efficient, runs smoothly on most systems

---

## 🛠️ Technologies Used

| Tool        | Purpose                            |
|-------------|-------------------------------------|
| Python      | Programming language                |
| OpenCV      | Real-time video processing          |
| MediaPipe   | Hand tracking and landmark detection|
| NumPy       | Numerical operations                |
| Math        | Geometrical calculations            |

---

## 📂 Folder Structure

```
finger-counter-project/
│
├── HandTrackingModule.py   # Custom module for hand detection
├── FingerCounter.py        # Main application file
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 🔧 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Peehuagrawal/finger-counter-project.git
cd finger-counter-project
```

2. **Install required dependencies:**

```bash
pip install -r requirements.txt
```

> Make sure you have Python 3.x installed.

---

### ▶️ Running the App

```bash
python FingerCounter.py
```

- Your webcam should turn on.
- Hold your hand up in front of the camera.
- Watch the screen to see how many fingers are detected.

---

## 🧰 How It Works

1. **Hand Detection:**  
   Uses MediaPipe to detect and track hand landmarks in real-time.

2. **Landmark Extraction:**  
   The `HandTrackingModule.py` extracts the x, y coordinates of 21 key points on the hand.

3. **Finger Logic:**  
   A simple rule-based system compares landmark positions to determine which fingers are open.

4. **Visualization:**  
   OpenCV overlays lines, circles, and the finger count text on the video feed.

---

## 📈 Possible Improvements

- ✅ Multi-hand detection
- ✅ Gesture recognition beyond finger counting
- ✅ Improved accuracy in low-light conditions
- ✅ Integration with smart home or IoT devices
- ✅ Add audio or haptic feedback

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use, modify, and share it.

---

## 🙋‍♀️ Author

**Peehu Agrawal**  
🌐 [GitHub Profile](https://github.com/Peehuagrawal)

---

> ⭐ *If you found this project interesting, don’t forget to give it a star on GitHub!*  
> 💬 *Feel free to open issues or contribute pull requests!*

