import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = None
public_key = None

def generate_keys():
    global private_key, public_key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    messagebox.showinfo("Success", "Keys Generated")

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

    messagebox.showinfo("Success", "File Signed")

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
        messagebox.showinfo("Result", "Verified OK")
    except:
        messagebox.showerror("Result", "Verification Failed")

root = tk.Tk()
root.title("Digital Signature Demo")

tk.Button(root, text="Generate Keys", command=generate_keys).pack()
tk.Button(root, text="Sign File", command=sign_file).pack()
tk.Button(root, text="Verify File", command=verify_file).pack()

root.mainloop()
