# Caesar Cipher

This script implements the Caesar cipher algorithm for both encryption and decryption. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- Encrypt or decrypt text using the Caesar cipher algorithm.
- Command-line interface for easy usage.
- Validation of input to ensure only alphabetic characters are processed.

## Usage

### Command-Line Arguments

- `-E`, `--encrypt` : Encrypt the provided text.
- `-D`, `--decrypt` : Decrypt the provided text.
- `text` : The text to encrypt or decrypt (must be alphabetic).
- `shift` : The number of positions each letter in the text is shifted.

### Examples

#### Encryption

To encrypt the text "hello" with a shift of 3:

```bash
python caesar_cipher.py -E "hello" 3
```

**Ouput:**
```
Ciphertext = khoor
```

## Requirements
- Python 3.x

## Implementation Details
- **Encryption:** Shifts each letter in the plaintext by the specified number of positions.
- **Decryption:** Shifts each letter in the ciphertext back by the specified number of positions.
- **Validation:** Ensures that only alphabetic characters are processed.

## Error Handling
- **Mutually Exclusive Actions:** You cannot specify both `-E` and `-D` options. You must choose one.
- **Invalid Input:** Only alphabetic characters are allowed in the text.

