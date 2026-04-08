import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = None
public_key = None
attacker_private = None
attacker_public = None

def generate_keys():
    global private_key, public_key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    messagebox.showinfo("Success", "Legitimate Keys Generated")

def attacker_keys():
    global attacker_private, attacker_public
    attacker_private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    attacker_public = attacker_private.public_key()
    messagebox.showinfo("Attack", "Attacker Keys Generated")

def sign_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    with open(file_path, "rb") as f:
        data = f.read()

    signature = private_key.sign(
        data,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    with open("signature.bin", "wb") as f:
        f.write(signature)

    messagebox.showinfo("Success", "File Signed (Legitimate)")

def attacker_sign():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    with open(file_path, "rb") as f:
        data = f.read()

    signature = attacker_private.sign(
        data,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    with open("signature.bin", "wb") as f:
        f.write(signature)

    messagebox.showinfo("Attack", "File Signed by Attacker")

def verify_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    with open(file_path, "rb") as f:
        data = f.read()

    with open("signature.bin", "rb") as f:
        signature = f.read()

    try:
        public_key.verify(
            signature,
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        messagebox.showinfo("Result", "Verified OK (Legitimate)")
    except:
        messagebox.showerror("Result", "Verification Failed")

def verify_with_attacker():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    with open(file_path, "rb") as f:
        data = f.read()

    with open("signature.bin", "rb") as f:
        signature = f.read()

    try:
        attacker_public.verify(
            signature,
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        messagebox.showinfo("Attack Result", "Verified OK (Key Substitution Attack)")
    except:
        messagebox.showerror("Attack Result", "Attack Failed")

root = tk.Tk()
root.title("Digital Signature + Key Substitution Attack")
root.geometry("400x420")

tk.Button(root, text="Generate Legitimate Keys", command=generate_keys).pack(pady=5)
tk.Button(root, text="Sign File (Legitimate)", command=sign_file).pack(pady=5)
tk.Button(root, text="Verify (Legitimate)", command=verify_file).pack(pady=5)

tk.Label(root, text="--- Attack Section ---").pack(pady=10)

tk.Button(root, text="Generate Attacker Keys", command=attacker_keys).pack(pady=5)
tk.Button(root, text="Attacker Sign File", command=attacker_sign).pack(pady=5)
tk.Button(root, text="Verify with Attacker Key", command=verify_with_attacker).pack(pady=5)

root.mainloop()
