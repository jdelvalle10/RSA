# RSA
Simple implementation of the RSA Asymmetric Encryption Algorithm

## RSA Encryption Implementation
This repository contains an implementation of the RSA encryption algorithm in Python. RSA (Rivest–Shamir–Adleman) is 
one of the first public-key cryptosystems and is widely used for secure data transmission.

## Features
Key Generation: Generate public and private keys.
Encryption: Encrypt plaintext messages using the public key.
Decryption: Decrypt ciphertext messages using the private key.

## Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your_username/your_repository.git

## Libraries Used

The `generate_keys.py` script relies on the following libraries:

- **Python Sympy**: This library provides symbolic math recipes and primitives to Python developers. It is used here top perform number theory operations, like finding large prime numbers required for generating secure cryptographic algorithms.

    - **Installation**: You can install Python Sympy using pip:

        ```bash
        pip install sympy
        ```

    - **Documentation**: https://www.sympy.org/en/index.html

- **Math**: This is a standard Python library used for mathematical operations. It is used in the RSA key generation process for computing modular arithmetic operations such as finding modular inverses and performing modular exponentiation.

    - **Installation**: The `math` library comes pre-installed with Python and does not require separate installation.

    - **Documentation**: [Python Math Library Documentation](https://docs.python.org/3/library/math.html)

- **Random**: Another standard Python library, `random` is used for generating random numbers. In the context of RSA key generation, it is used to select prime numbers and randomize the key generation process.

    - **Installation**: Like `math`, the `random` library is part of the Python standard library and does not require separate installation.

    - **Documentation**: [Python Random Library Documentation](https://docs.python.org/3/library/random.html)

These libraries are essential for the generation of RSA key pairs, ensuring the security and integrity of the generated keys.

bash
Copy code
## Usage
* Start with the generate_keys.py program. This will ask you the size of the prime numbers (in bits) needed to generate the public/private key pair. You will see two files generated, one with the public key (a tuple) and other with the private key. 
* Now create a "message.txt" file containing a message you want to send 
* Use the Encrypt.py program will use Alice's public key to encrypt it and return another file: "encrypted_message.txt"
* Use the Decrypt.py program to decrypt the message, this time using Alice's private key. This will return a file with the decrypted message.

## Contributing
Contributions are welcome! Please follow these steps:

* Fork the repository.
* Create a new branch (git checkout -b feature/your_feature).
* Make your changes.
* Commit your changes (git commit -am 'Add some feature').
* Push to the branch (git push origin feature/your_feature).
* Create a new Pull Request.

## License
MIT

