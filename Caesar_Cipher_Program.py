# Caesar Cipher Implementation

def caesar_cipher(text, shift, mode):
    if mode == 'decrypt':
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Choose mode ('encrypt' or 'decrypt'): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
        return

    text = input("Enter the message: ").strip()
    try:
        shift = int(input("Enter the shift value (integer): ").strip())
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        return

    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
