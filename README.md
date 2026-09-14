```markdown

# 🔥 ADVANCE-NUM-LOOKUP

**Check if your mobile number was leaked in a data breach.**

**Made by ANURAG X NOTHING**


---

## ⚠️ Read This First

> This tool is only for checking YOUR OWN number.
> Checking someone else's number is illegal.
> The developer is not responsible if you misuse this tool.

---

## 📌 What Is This Tool?

ADVANCE-NUM-LOOKUP is a terminal tool. You give it a mobile number. It checks public data breach records. Then it tells you if that number was leaked, and what details were leaked — name, father's name, address, circle, email.

---

## ⚡ Features

- Fast Lookup — result in a few seconds
- Full Details — name, father's name, address, circle, email
- Bulk Check — check many numbers from one file
- Auto Save — saves result as JSON and TXT file
- Clean UI — nice colors and tables in terminal
- Works on Termux — Android support, no root needed
- Session Stats — see how many lookups you did
- Protected Branding — developer credits are locked
```

📱 Installation — Termux (Android)

Step 1 — Update Termux

```bash
pkg update -y && pkg upgrade -y
```

Step 2 — Install Python and Git

```bash
pkg install python git -y
```

Step 3 — Clone the Repository

```bash
git clone https://github.com/urcybernothing/ADVANCE-NUM-LOOKUP-.git
```

Step 4 — Go Into the Folder

```bash
cd ADVANCE-NUM-LOOKUP-
```

Step 5 — Install Required Packages

```bash
pip install -r requirements.txt
```

If that fails, try:

```bash
pip install requests rich pyfiglet
```

Step 6 — Run the Tool

```bash
python anurix.py
```

---

🐧 Installation — Linux

Step 1

```bash
sudo apt update && sudo apt upgrade -y
```

Step 2

```bash
sudo apt install python3 python3-pip git -y
```

Step 3

```bash
git clone https://github.com/urcybernothing/ADVANCE-NUM-LOOKUP-.git
```

Step 4

```bash
cd ADVANCE-NUM-LOOKUP-
```

Step 5

```bash
pip3 install -r requirements.txt
```

Step 6

```bash
python3 anurix.py
```

---

🎮 How To Use

Start the tool:

```bash
python anurix.py
```

Menu will open:

```
[1] Check One Number
[2] Check Many Numbers (from file)
[3] About Developer
[4] Session Stats
[5] Exit
```

Option 1 — Type 1, press Enter, type 10-digit number, press Enter. Result shows.

Option 2 — Make a text file numbers.txt with one number per line. Choose option 2. Give the file path. Tool checks all.

Option 3 — Shows developer info and channels.

Option 4 — Shows session stats.

Option 5 — Exit.

---

📁 Where Are Results Saved?

All results go into the exports/ folder. Each lookup makes two files — one .json and one .txt.

To see saved files:

```bash
ls exports/
```

---

🔧 Common Problems

git: command not found → pkg install git -y

python: command not found → pkg install python -y

pip: command not found → pkg install python -y

ModuleNotFoundError → pip install -r requirements.txt

Permission denied → chmod +x anurix.py

Connection error → Internet check kar, ya API down hai, thodi der baad try kar.

---

🗂️ Project Files

File What It Does
anurix.py Main tool
requirements.txt Python packages list
install.sh Auto installer
README.md Instructions
LICENSE MIT license
.gitignore Git ignore rules

---

🌐 Developer and Channels

Platform Handle Link
Telegram @anonymousanurix https://t.me/anonymousanurix
Telegram @hackedanurag https://t.me/hackedanurag
Instagram @hackedxanu https://www.instagram.com/hackedxanu

---

⚠️ Legal Warning

Use this tool only for your own number.

· Checking your own number — allowed
· Checking someone else's number — illegal
· Using it for stalking or doxxing — illegal

The developer (ANURAG X NOTHING) is not responsible for any misuse.

---

📜 License

MIT License. See the LICENSE file for full text.

Keep the developer credits. Do not remove them.

---

<div align="center">

🔥 ANURIX — Where information lives 🔥

Join: https://t.me/anonymousanurix

© 2025 ANURIX — All Rights Reserved

</div>
```
