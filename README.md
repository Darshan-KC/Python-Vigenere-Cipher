# Python Vigenère Cipher

This repository contains a Python implementation of the Vigenère Cipher, a classic cryptographic technique for encoding and decoding messages. This program is optimized and implemented without relying on external libraries, offering a clean and straightforward approach to encryption and decryption.

---

## Features

- **Encrypt messages** using the Vigenère Cipher algorithm.
- **Decrypt messages** to retrieve the original text.
- **Custom key support** for personalized encryption.
- Simple and efficient implementation in Python.

---

## Table of Contents

- [About the Vigenère Cipher](#about-the-vigenère-cipher)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## About the Vigenère Cipher

The Vigenère Cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt a message. Each letter in the plaintext is shifted by a value determined by the corresponding letter in the key, creating a more secure encryption than simple substitution ciphers.

---

## Requirements

- Python 3.x

No additional libraries or dependencies are required.

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Darshan-KC/Python-Vigenere-Cipher.git
    cd Python-Vigenere-Cipher
    ```

2. Ensure you have Python 3.x installed.

---

## Usage

Run the program using Python:

```bash
python vigenere_cipher.py
```

You can follow the prompts to either encrypt or decrypt a message.

---

## Examples

### Encrypting a Message

Input:
```
Enter plaintext: HELLO
Enter key: KEY
```
Output:
```
Encrypted text: RIJVS
```

### Decrypting a Message

Input:
```
Enter ciphertext: RIJVS
Enter key: KEY
```
Output:
```
Decrypted text: HELLO
```

---

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository, make changes, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
