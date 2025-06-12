# PasswordsMatrix
It is about how I used matrices to create strong passwords


A quirky, personal, and powerful password generator based on matrix determinants and ASCII values — inspired by high school math and powered by Python.

> 💡 Ever wanted to generate a secure password using something *you* can remember — like a favorite name, phrase, or number? This tool does exactly that.

---

## ✨ What It Does

PasswordsMatrix:
- Takes a 9-character input (word, phrase, name+number combo)
- Arranges it into a 3x3 matrix
- Converts each character into its ASCII code
- Calculates the determinant of that matrix
- Transforms the result into a strong password using your **custom digit-to-symbol substitution map**
- Lets you optionally add a memory-based prefix or suffix for easy recall

---

## 🧠 Example
Input word: `RamCharan`

Custom digit substitutions:
```
1 → !
2 → %
3 → #
5 → @
```

Prefix: `RAM`, Suffix: `CSK`

Generated Password: `RAM@#!%@CSK` (varies based on matrix determinant)

---

## 🚀 How to Run

### Requirements
- Python 3.x
- `numpy`

### Run the Generator
```bash
python passwords_matrix.py
```
Follow the prompts to:
- Enter a **9-character word or phrase**
- Customize symbol replacements for each digit (optional — defaults provided)
- Add a **prefix** (memory cue) or a **suffix** (like a favorite team or show)

---

## 📁 Files
- `passwords_matrix.py` — The main Python script

---

## 🧩 How It Works
1. Converts your 9-letter string into a 3x3 ASCII matrix
2. Computes the determinant of the matrix
3. Maps the digits of the determinant to symbols using your custom map
4. Wraps it with your personal memory-based prefix and suffix

---

## 🤝 Credits
- 🧠 Idea: You! (Inspired by playing with matrices in high school)
- 🤖 Help & Coding Assistant: ChatGPT (aka Jon, your AI bro)

---

## 🧵 Spread the Word
- Share your custom passwords story on **Medium**
- Post cool examples or generator screenshots on **Twitter** or **Instagram**

---

## 🛡️ Final Thoughts
This tool is designed for **creativity + security**. It gives you:
- Something memorable
- Something unique
- And something **only you** can reverse-engineer 💥

> Customize your password... like a legend.

**Stay secure. Stay quirky. Stay you.** 🔒
