import argparse

def verify_input(input_string):
    # Check if input contains at least one letter and is not purely numeric
    has_letter = any(char.isalpha() for char in input_string)
    is_numeric = input_string.isdigit()
    
    # Return True if the input has at least one letter and is not purely numeric
    return has_letter and not is_numeric

def encrypt_caesar(plain, shift):
    cipher = str()
    for letter in plain:
        if letter.isupper():
            cipher += chr(((ord(letter) - 65) + shift) % 26 + 65)
        elif letter.islower():
            cipher += chr(((ord(letter) - 97) + shift) % 26 + 97)
        else:
            cipher+=letter # Return non-alphabetic characters as they are
    return cipher 

def decrypt_caesar(cipher, shift):
    plain = str()
    
    for letter in cipher:
        if letter.isupper():
            plain += chr(((ord(letter) - 65) - shift) % 26 + 65)
        elif letter.islower():
            plain += chr(((ord(letter) - 97) - shift) % 26 + 97)
        else:
            plain+=letter # Return non-alphabetic characters as they are
    return plain 

def main():
    parser = argparse.ArgumentParser(description='Caesar cipher encryption and decryption.')
    
    # Add optional arguments
    parser.add_argument('-E', '--encrypt', action='store_true', help='Encrypt the text.')
    parser.add_argument('-D', '--decrypt', action='store_true', help='Decrypt the text.')
    parser.add_argument('text', type=str, help='The text to encrypt or decrypt.')
    parser.add_argument('shift', type=int, help='The shift value for the Caesar cipher.')

    # Analyze arguments
    args = parser.parse_args()

    # Check for mutually exclusive actions
    if args.encrypt and args.decrypt:
        print("Error: You cannot specify both -E and -D options.")
        return

    if not args.encrypt and not args.decrypt:
        print("Error: You must specify either -E or -D option.")
        return

    # Verify the validity of the text
    if not verify_input(args.text):
        print("Invalid input. Please enter only letters (uppercase or lowercase).")
        return
    
    # Execute the chosen action
    if args.encrypt:
        result = encrypt_caesar(args.text, args.shift)
        print("Ciphertext =", result)
    elif args.decrypt:
        result = decrypt_caesar(args.text, args.shift)
        print("Plaintext =", result)

if __name__ == "__main__":
    main()