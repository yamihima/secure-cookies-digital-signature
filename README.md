# 🔐 Secure Cookies & Digital Signature System

A complete implementation of a **secure web system** that demonstrates two fundamental cryptography concepts:

1. **Cookie Protection** using HMAC-SHA256 (Message Authentication Code)
2. **File Integrity & Authenticity** using RSA Digital Signatures

## ✨ Features

### 🍪 Part A: HMAC-Secured Cookies
- Login mechanism with username/role-based cookies
- HMAC-SHA256 tag generation using a server-side secret key
- Automatic tamper detection – any manual cookie modification (e.g., role change) rejects the request
- Secret key never leaves the server (no plain hashing)

### 🔏 Part B: RSA Digital Signatures
- RSA key pair generation (private + public keys)
- File signing using SHA-256 with private key
- Signature verification using public key
- Demonstrates both success (original file) and failure (modified file)

### 🎯 Bonus: Key Substitution Attack
- GUI-based demonstration of the vulnerability described in Wong (Page 150)
- Shows how a maliciously crafted public key can falsely verify a forged signature
- Includes explanation of the attack mechanics

## 🛠️ Tech Stack
- **Language:** Python 100%
- **Libraries:** Flask, cryptography, hashlib, hmac, tkinter (GUI)
- **Cryptography:** RSA, HMAC-SHA256

## 📂 Project Structure
secure-cookies-digital-signature/
├── app.py # Flask web app for HMAC cookies
├── digital_signature.py # RSA signing & verification CLI
├── gui_signer.py # Bonus attack GUI demo
├── *.png # Screenshots of successful runs
└── README.md

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/ibrahimmahmoudzaki/secure-cookies-digital-signature.git
cd secure-cookies-digital-signature

# Install dependencies
pip install flask cryptography

# Run HMAC cookie demo
python app.py

# Run digital signature demo
python digital_signature.py

# Run bonus attack GUI
python gui_signer.py
