from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import tkinter as tk
from tkinter import filedialog

key = RSA.generate(3072)
private_key = key.exportKey()
public_key = key.publickey().exportKey()
with open('./keys/privateKey.pem', 'wb') as private_file:
    private_file.write(private_key)
with open('./keys/publicKey.pem', 'wb') as public_file:
    public_file.write(public_key)


def decrypt(encrypted):
    private_key = RSA.importKey(open("./keys/privateKey.pem").read())
    decryptor = PKCS1_OAEP.new(private_key)
    decrypted = decryptor.decrypt(encrypted)
    return decrypted

def encrypt(msg):
    public_key = RSA.importKey(open("./keys/publicKey.pem").read())
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



root = tk.Tk()
root.title("RSA Encryption Tool")

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


root.mainloop()
