# 🎤 AI Voice-Controlled Email Assistant

An intelligent Python-based automation tool that listens to your voice, converts it to text using speech recognition, and sends the message via email automatically.

---

## 📌 Features
- **Voice-to-Text** using Google Speech Recognition API
- **Ambient Noise Cancellation** for better accuracy
- **Automated Email Sending** via Gmail using `yagmail`
- **Error Handling** for speech and network failures
- **Secure Authentication** with Gmail App Passwords
---

## 🛠 Tech Stack
- **Python 3.12**
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/)
- [`yagmail`](https://pypi.org/project/yagmail/)
- Google Speech API

---

## 📂 Project Structure
email-voice-assistant/
├── main.py # Main script
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── .gitignore # Ignored files

yaml
Copy
Edit

---

## 🚀 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ananthshetty2002/AIspeech.git
cd AIspeech
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Generate a Gmail App Password
Enable 2-Step Verification on your Gmail account

Go to Google App Passwords

Generate a 16-character password for "Mail"

Use it in the script instead of your normal Gmail password

4️⃣ Run the Script
bash
Copy
Edit
python main.py
📹 Demo Video
🎥 Watch the Demo on YouTube

📌 Example Output
arduino
Copy
Edit
🔊 Clearing background noise...
🎙️ Waiting for your message...
🧾 Transcribing message...
✅ Your message: You are the best
📨 Sending email...
✅ Mail sent successfully!
🔐 Security Note
Never commit your Gmail password to GitHub

Always use environment variables or an .env file for sensitive credentials

Use Gmail App Passwords instead of your main account password

📜 License
This project is licensed under the MIT License — feel free to use and modify it.

🤝 Connect
Developed by Ananth Shetty
📧 Email: shettyananth24@gmail.com
🌐 LinkedIn: Your LinkedIn Profile
