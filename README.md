# 🔐 Project Encoder-Decoder

A simple yet fun Python project that encodes and decodes secret messages using a custom word-based encoding scheme. Perfect for beginners exploring Python string manipulation, logic building, and basic CLI interaction!

---

## 📌 Table of Contents

[![About](https://img.shields.io/badge/📖-About-blue?style=for-the-badge)](#-about)  
[![Features](https://img.shields.io/badge/✨-Features-green?style=for-the-badge)](#-features)  
[![How It Works](https://img.shields.io/badge/⚙️-How_It_Works-orange?style=for-the-badge)](#️-how-it-works)  
[![Getting Started](https://img.shields.io/badge/🚀-Getting_Started-yellow?style=for-the-badge)](#-getting-started)  
[![Usage Examples](https://img.shields.io/badge/🧪-Usage_Examples-purple?style=for-the-badge)](#-usage-examples)  
[![File Structure](https://img.shields.io/badge/📂-File_Structure-lightgrey?style=for-the-badge)](#-file-structure)  
[![Technologies Used](https://img.shields.io/badge/🛠️-Technologies_Used-brightgreen?style=for-the-badge)](#️-technologies-used)  
[![Future Improvements](https://img.shields.io/badge/📝-Future_Improvements-blueviolet?style=for-the-badge)](#-future-improvements)  
[![Author](https://img.shields.io/badge/🙋‍♂️-Author-ff69b4?style=for-the-badge)](#-author)  
[![Need Help](https://img.shields.io/badge/💬-Need_Help-cyan?style=for-the-badge)](#-need-help)

---

## 📖 About

**Project Encoder-Decoder** is a command-line tool that lets users encode their messages in a simple obfuscated format and decode them back to the original. It applies logic similar to ROT13 or Pig Latin, but with a custom twist involving string rearrangement and random noise.

---

## ✨ Features

- 🔁 Two-way encoding/decoding of words  
- 🧠 Custom string-based encoding logic  
- 🔒 Adds random characters to mask the original message  
- 📏 Special handling for short words (less than 3 letters)  
- 🧪 CLI-based interactive interface  

---

## ⚙️ How It Works

### Encoding Logic:
1. If the word has **less than 3 letters**, it’s simply **reversed**.
2. If the word has **3 or more letters**:
   - First letter is moved to the end.
   - Three **random letters** are added at the beginning and the end to obfuscate it.

### Decoding Logic:
- Strips the random characters.
- Moves the last character (which was the original first letter) back to the front.

---

## 🚀 Getting Started

### 📥 Prerequisites
Make sure you have Python installed:

```bash
python --version
```

### ⬇️ Clone the Repository

```bash
git clone https://github.com/aaryan498/Project-Encoder-Decoder.git
cd Project-Encoder-Decoder
```

### ▶️ Run the Program

```bash
python coder.py
```

---

## 🧪 Usage Examples

### 🧬 Encoding:
```
Enter your choice: encode
Write your message to be encoded here:
hello world
Encoded Message:
aBqellohEw xRyorldwFy
```

### 🔓 Decoding:
```
Enter your choice: decode
Write your message to be decoded here:
aBqellohEw xRyorldwFy
Decoded Message:
hello world
```

---

## 📂 File Structure

```
Project-Encoder-Decoder/
├── coder.py                # Main Python script
└── README.md               # Project documentation
```

---

## 🛠️ Technologies Used

- 🐍 Python 3
- `random` and `string` modules for character generation

---

## 📝 Future Improvements

- 🖼️ GUI version using Tkinter or PyQt  
- 🌐 Web version using Flask or Streamlit  
- 🔐 Add encryption-grade encoding options  
- 🧪 Unit testing and better error handling  

---

## 🙋‍♂️ Author

[![Aaryan Kumar - GitHub](https://img.shields.io/badge/GitHub-aaryan_kumar-181717?logo=github&style=for-the-badge)](https://github.com/aaryan498)

---

## 💬 Need Help?

If you face any **errors** while running the project or get stuck at any point, feel free to reach out in the **comment section** of my LinkedIn project post linked below. I’ll be happy to help you there!

[![Comment on LinkedIn](https://img.shields.io/badge/💬%20Ask%20on%20LinkedIn-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/posts/aaryan-kumar-ai-498-coder_python-opensource-beginnerprojects-activity-7355539933119344640-s_ET?utm_source=share&utm_medium=member_android&rcm=ACoAAFxqlpgBiTnkrCNekCuz5lwACzH6vXUUKvA)

---

> 💡 *If you like this project, give it a ⭐ on GitHub and let others know!*
