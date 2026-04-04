import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# 1. Key-Pair Generation [cite: 47]
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

# 2. File Signing [cite: 48]
def sign_data(private_key, data):
    signature = private_key.sign(
        data,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return signature

# 3. Signature Verification 
def verify_signature(public_key, data, signature):
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True # Successful verification [cite: 49]
    except Exception:
        return False # Verification failure after modification [cite: 51]

# --- PART B DEMONSTRATION ---
priv, pub = generate_keys()
original_data = b"Student Assignment Data"

# Sign the file [cite: 40, 41]
sig = sign_data(priv, original_data)
print(f"Original Verification: {verify_signature(pub, original_data, sig)}")

# Tamper with the file [cite: 50]
tampered_data = b"Student Assignment Date" # Changed 'a' to 'e'
print(f"Tampered Verification: {verify_signature(pub, tampered_data, sig)}")
