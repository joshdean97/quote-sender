# ✉️ Quote Sender

Random quotes. Delivered. Daily.

> _“Words are free. It’s how you use them that may cost you.”_

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)

---

## 🧠 What is Quote Sender?

Quote Sender is a lightweight Python app that grabs a random quote from a JSON file and delivers it via your preferred method — email, terminal, or even AWS SNS. Whether you're building a daily motivation system or spamming your team with wisdom, this tool has your back.

## ✨ Features

- 🗂️ Loads quotes from a `quotes.json` file
- 🔀 Sends a random quote each time
- ☁️ Supports AWS SNS for cloud-based quote delivery
- 🧪 Simple, modular, and testable
- 🔧 Easily extendable for email, SMS, or other integrations

## 🛠️ Tech Stack

- **Language**: Python 3.11
- **Cloud Integration**: AWS SNS (optional)
- **Data**: JSON quote storage
- **OS**: Windows-compatible

## 🚀 Getting Started

### Clone the repo

<pre>```bash
git clone https://github.com/yourusername/quote-sender.git
cd quote-sender
```</pre>

### Install Dependencies
<pre>```bash
pip install -r requirements.txt
```</pre>

### Run the app
<pre>```bash
python quote_sender.py
```</pre>

### 🔧 Configuration
<pre>```.env
Make sure you set up your environment variables or .env:
AWS_ACCESS_KEY_ID=youraccesskey
AWS_SECRET_ACCESS_KEY=yoursecretkey
SNS_TOPIC_ARN=arn:aws:sns:region:account-id:topicname
```</pre>
### 🗃️ Example quotes.json
<pre>```json
[
  {
    "Quote": "Don't cry because it's over, smile because it happened.",
    "Author": "Dr. Seuss"
  },
  {
    "Quote": "Be yourself; everyone else is already taken.",
    "Author": "Oscar Wilde"
  }
]
```</pre>
🤝 Contributing
Got a quote you love? Want to build an email module or web dashboard?

- Fork it 🍴

- Create your branch: git checkout -b feature/awesome

- Commit changes: git commit -m "Added epic feature"

- Push to the branch: git push origin feature/awesome

- Submit a Pull Request 🧠

📜 License
MIT — do whatever you want, just don’t be evil.

🧠 Author
Built with 🤓 and ☕ by Josh Shep.

“Keep your face always toward the sunshine—and shadows will fall behind you.” – Walt Whitman

⭐ Star this repo if it made you smile today!
