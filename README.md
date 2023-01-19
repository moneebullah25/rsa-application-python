# rsa-application-python
**RSA Encryption Tool**

This application is a simple RSA encryption tool that allows the user to encrypt and decrypt files using RSA encryption. The tool also allows the user to encrypt and decrypt plain text messages. The tool has a simple graphical user interface built with tkinter.

**Getting Started**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

**Prerequisites**

- Python 3.x
- Pycryptodome library

**Installing**

- Install python on your local machine
- Install pycryptodome library

Copy code

pip install pycryptodome 

- Clone the repository to your local machine

Copy code
https://github.com/moneebullah25/rsa-application-python.git

- Run the script

Copy code

python rsa\_encryption\_tool.py 

**Using the tool**

- To encrypt a file, click the "Encrypt File" button and select the file you want to encrypt. The encrypted file will be saved with the extension ".encrypted" in the same directory as the original file.
- To decrypt a file, click the "Decrypt File" button and select the file you want to decrypt. The decrypted file will be saved in the same directory as the original file with the extension removed.
- To encrypt a message, enter the plain text message in the "Plain Text" text widget and click the "Encrypt" button. The encrypted message will be displayed in the "Encrypted Text" text widget.
- To read a plain text file, click the "Read from File" button and select the file you want to read. The contents of the file will be displayed in the "Plain Text" text widget.
- To save an encrypted message to a file, click the "Save to File" button and select the location where you want to save the file.
- Click on the "Sign" button to sign the plain text message and display the signature in the "Signature Text" field.
- Click on the "Verify" button to verify the signature of the plain text message. The tool will display the result if the signature is valid or not.
- To generate new RSA keys, click on the "Generate Keys" button. These keys will be saved in the "keys" folder.
- To load the existing keys, click on the "Load Keys" button. From that point these loaded keys will be used.

**Built With**

- [Python](https://www.python.org/) - The programming language used
- [Pycryptodome](https://pycryptodome.org/en/latest/src/introduction.html) - The encryption library used
- [Tkinter](https://docs.python.org/3/library/tk.html) - The library used for the GUI
- [Filedialog](https://docs.python.org/3/library/tkinter.filedialog.html) - The library used for the file dialogs

**References**

- [Pycryptodome RSA documentation](https://pycryptodome.org/en/latest/src/public_key/rsa.html)
- [Tkinter documentation](https://docs.python.org/3/library/tk.html)
- [Filedialog documentation](https://docs.python.org/3/library/tkinter.filedialog.html)
- [Python documentation](https://docs.python.org/3/)

**License**

This project is licensed under the MIT License - see the [LICENSE.md](https://chat.openai.com/chat/LICENSE.md) file for details.
