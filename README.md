# Caesar Cipher Program

## Introduction
The **Caesar Cipher Program** is a Python-based encryption and decryption tool that implements the classic Caesar cipher technique. The program shifts each letter in the text by a fixed number of positions in the alphabet, providing a simple yet effective method of encoding messages.

## Features
- Encrypts plain text using the Caesar cipher.
- Decrypts encrypted text back to the original message.
- Supports user-defined shift values.
- Works with uppercase and lowercase letters.
- Ignores non-alphabetical characters.

## How It Works
The Caesar cipher is a substitution cipher that shifts the letters in the alphabet by a set number of positions. For example, with a shift of **3**:
- `A` → `D`
- `B` → `E`
- `C` → `F`

To decrypt, the letters are shifted back by the same number.

## Installation
To use this program, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Usage
1. Clone or download this repository.
2. Navigate to the directory containing `Caesar_Cipher_Program.py`.
3. Run the script using the following command:
   ```sh
   python Caesar_Cipher_Program.py
   ```
4. Enter the message you want to encrypt or decrypt.
5. Provide a shift value.
6. View the output message.

## Example
**Input:**
```
Enter 'E' for encryption or 'D' for decryption: E
Enter your message: HELLO
Enter shift value: 3
```

**Output:**
```
Encrypted message: KHOOR
```


