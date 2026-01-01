🖱️ AI Virtual Mouse Using Hand Gestures

A computer vision–based virtual mouse that allows you to control your system cursor using hand gestures via webcam.
Built using Python, OpenCV, MediaPipe, and PyAutoGUI.

🚀 Features

✅ Smooth & accurate mouse movement
✅ Left click using thumb + index finger
✅ Right click using middle finger
✅ Scroll up/down using finger gestures
✅ Noise-free movement (anti-shake smoothing)
✅ Works on low-end systems
✅ No external hardware required

🧠 Technology Stack

Python 3.10

OpenCV – camera & image processing

MediaPipe – hand tracking

PyAutoGUI – mouse control

Math & Time – gesture logic

📁 Project Structure
KaranVirtualMouse/
│
├── mouse.py        # Main program
├── README.md       # Project documentation

⚙️ Installation Guide
✅ Step 1: Install Python (IMPORTANT)

Use Python 3.10.11

👉 Download:
https://www.python.org/downloads/release/python-31011/

✔ Tick Add Python to PATH during installation

✅ Step 2: Install Required Libraries

Open Command Prompt and run:

pip install mediapipe opencv-python pyautogui

▶️ How to Run the Project

Open the project folder

Open terminal inside it

Run:

python mouse.py

🖐️ Gesture Controls
Gesture	Action
Index finger move	Move mouse
Thumb + Index	Left click
Middle + Index	Right click
Middle finger up/down	Scroll
Press Q	Exit program
⚡ Best Performance Tips

✔ Use good lighting
✔ Keep hand 40–60 cm from camera
✔ Use plain background
✔ Avoid shaking hand
✔ Use one hand only

🧩 Code Highlights

Exponential smoothing for smooth movement

Click debounce to avoid accidental clicks

Real-time hand landmark tracking

Optimized for low latency

🛠️ Known Issues

Works best in good lighting

Webcam quality affects accuracy

Not recommended for gaming

🚀 Future Improvements

Gesture-based volume control

Virtual keyboard

Multi-hand support

GUI settings panel

AI gesture calibration

👨‍💻 Author

Karan Tomar
🎓 Computer Science & Design
💡 AI & Automation Enthusiast

⭐ Support

If you like this project:

⭐ Star this repository

🍴 Fork it

🧠 Improve it

📜 License

This project is open-source and free to use for learning purpose.
