from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox

def generateKeys():
    key = RSA.generate(3072)
    private_key = key.exportKey()
    public_key = key.publickey().exportKey()
    with open('./keys/privateKey.pem', 'wb') as private_file:
        private_file.write(private_key)
    with open('./keys/publicKey.pem', 'wb') as public_file:
        public_file.write(public_key)

def loadKeys():
    with open('./keys/privateKey.pem', 'rb') as private_file:
        private_key = RSA.importKey(private_file.read())
    with open('./keys/publicKey.pem', 'rb') as public_file:
        public_key = RSA.importKey(public_file.read())
    return private_key, public_key

def decrypt(encrypted):
    private_key = RSA.importKey(open("./keys/privateKey.pem").read())
    if not private_key:
        messagebox.showerror("Could find keys in keys/ directory")
    decryptor = PKCS1_OAEP.new(private_key)
    decrypted = decryptor.decrypt(encrypted)
    return decrypted

def encrypt(msg):
    public_key = RSA.importKey(open("./keys/publicKey.pem").read())
    if not public_key:
        messagebox.showerror("Could find keys in keys/ directory")
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(msg)
    return encrypted

def encrypt_file():
    # get the file path of the file to encrypt
    filepath = filedialog.askopenfilename()
    if filepath:
        # read the plain text from the file
        with open(filepath, 'r') as file:
            plain_text = file.read()
        # encrypt the plain text
        crypto = binascii.hexlify(encrypt(plain_text.encode()))
        # save the encrypted text to a new file
        new_filepath = filepath + '.encrypted'
        with open(new_filepath, 'wb') as file:
            file.write(crypto)


def decrypt_file():
    # get the file path of the file to decrypt
    filepath = filedialog.askopenfilename()
    if filepath:
        # read the encrypted text from the file
        with open(filepath, 'rb') as file:
            crypto = file.read()
            
        plain_text = decrypt(binascii.unhexlify(crypto))

        new_filepath = filepath.replace('.encrypted', '')
        with open(new_filepath, 'w') as file:
            file.write(str(plain_text)[2:-1])


def encrypt_message():
    plain_text_message = plain_text.get("1.0", tk.END) # get the plain text message from the text widget
    encrypted_message = binascii.hexlify(encrypt(plain_text_message.encode()))
    encrypted_text.delete("1.0", tk.END) # clear the text widget
    encrypted_text.insert(tk.INSERT, encrypted_message) # insert the encrypted message


def read_file():
    file = filedialog.askopenfile(mode='r', filetypes=[("Text Files", "*.txt")])
    if file is None:
        return
    plain_text.delete("1.0", tk.END) # clear the text widget
    plain_text.insert(tk.INSERT, file.read())
    file.close()


def save_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    with open(filename, "wb") as file:
        crypto = encrypted_text.get("1.0", tk.END) # get the encrypted text from the text widget
        crypto = crypto.encode()
        file.write(crypto)


def verify_message():
    plain_text_message = plain_text.get("1.0", tk.END) # get the plain text message from the text widget
    signature = signature_text.get("1.0", tk.END)
    signature = bytes.fromhex(signature)
    h = SHA256.new(plain_text_message.encode())
    key = RSA.importKey(open("./keys/publicKey.pem").read()) # import the private key from file
    if not key:
        messagebox.showerror("Could find keys in keys/ directory")
    try:
        pkcs1_15.new(key).verify(h, signature)
        messagebox.showinfo("Verify Successful", "The signature is valid.")
    except:
        messagebox.showerror("Verify Failed", "The signature is not valid.")


def sign_message():
    plain_text_message = plain_text.get("1.0", tk.END) # get the plain text message from the text widget
    h = SHA256.new(plain_text_message.encode())
    key = RSA.importKey(open("./keys/privateKey.pem").read()) # import the private key from file
    if not key:
        messagebox.showerror("Could find keys in keys/ directory")
    signature = pkcs1_15.new(key).sign(h)
    signature_text.delete("1.0", tk.END) # clear the text widget
    signature_text.insert(tk.INSERT, signature.hex())



root = tk.Tk()
root.title("RSA Encryption Tool")

# Create a button to generate keys
generate_keys_button = tk.Button(root, text="Generate Keys", command=generateKeys)
generate_keys_button.pack()

# Create a button to load keys
load_keys_button = tk.Button(root, text="Load Keys", command=loadKeys)
load_keys_button.pack()

# Create a button to encrypt the file
encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt_file)
encrypt_button.pack()

# Create a button to decrypt the file
decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_file)
decrypt_button.pack()

# Create a label and a text widget for the plain text
plain_text_label = tk.Label(root, text="Plain Text:")
plain_text_label.pack()
plain_text = tk.Text(root, height=10, width=50)
plain_text.pack()

# Create a label and a text widget for the encrypted text
encrypted_text_label = tk.Label(root, text="Encrypted Text:")
encrypted_text_label.pack()
encrypted_text = tk.Text(root, height=10, width=50)
encrypted_text.pack()


# Create a button to encrypt the message
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.pack()

# Create a button to save the encrypted text to a file
save_file_button = tk.Button(root, text="Save to File", command=save_file)
save_file_button.pack()

# Create a button to read the encrypted text from a file
read_file_button = tk.Button(root, text="Read from File", command=read_file)
read_file_button.pack()


# Create a button to sign the message
sign_button = tk.Button(root, text="Sign", command=sign_message)
sign_button.pack()

# Create a label for signature text
signature_text_label = tk.Label(root, text="Signature Text")
signature_text_label.pack()
signature_text = tk.Text(root, height=1, width=50)
signature_text.pack()

# Create a button to verify the message
verify_button = tk.Button(root, text="Verify", command=verify_message)
verify_button.pack()

root.mainloop()
