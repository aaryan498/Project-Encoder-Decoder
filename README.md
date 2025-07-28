# 🔐 Project Encoder-Decoder

A simple yet fun Python project that encodes and decodes secret messages using a custom word-based encoding scheme. Perfect for beginners exploring Python string manipulation, logic building, and basic CLI interaction!

---

## 📌 Table of Contents

- [📖 About](#-about)
- [✨ Features](#-features)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Getting Started](#-getting-started)
- [🧪 Usage Examples](#-usage-examples)
- [📂 File Structure](#-file-structure)
- [🛠️ Technologies Used](#️-technologies-used)
- [📝 Future Improvements](#-future-improvements)
- [🙋‍♂️ Author](#-author)

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

**Aaryan Kumar**  
🌐 [GitHub](https://github.com/aaryan498)

---

> 💡 *If you like this project, feel free to give it a ⭐ on GitHub and share your feedback!*
