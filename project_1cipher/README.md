# Vigenère Cipher Implementation

This project demonstrates the implementation of the **Vigenère Cipher**,
a method of encrypting and decrypting alphabetic text using a keyword.

## Files

-   **main.py**: Contains the encryption and decryption functions as
    well as an example execution.

## How It Works

1.  The `vigenere()` function performs the core encryption/decryption
    process.
2.  The `encrypt()` function wraps around `vigenere()` for encryption.
3.  The `decrypt()` function wraps around `vigenere()` for decryption.
4.  A sample ciphertext is decrypted using the provided custom key.

## Functions

-   `vigenere(message, key, direction=1)`\
    Performs the Vigenère cipher. The `direction` argument determines
    whether to encrypt (`1`) or decrypt (`-1`).

-   `encrypt(message, key)`\
    Encrypts a given message using the specified key.

-   `decrypt(message, key)`\
    Decrypts a given message using the specified key.

## Example

``` python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

print(f'Encrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'Decrypted text: {decryption}')
```

## Output

    Encrypted text: mrttaqrhknsw ih puggrur
    Key: happycoding
    Decrypted text: programming is fun

------------------------------------------------------------------------

Enjoy encrypting and decrypting messages with your own custom key!
