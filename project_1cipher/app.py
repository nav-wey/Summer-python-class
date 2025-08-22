# Ciphertext to decrypt
text = 'mrttaqrhknsw ih puggrur'
# Custom key used for the Vigenère cipher
custom_key = 'happycoding'


def vigenere(message, key, direction=1):
    """
    A function that performs Vigenère cipher encryption or decryption.

    Args:
        message (str): The text to be encrypted/decrypted.
        key (str): The keyword used for the cipher.
        direction (int): 1 for encryption, -1 for decryption.

    Returns:
        str: The processed (encrypted or decrypted) message.
    """
    key_index = 0  # Keeps track of which letter of the key is being used
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Alphabet set
    final_message = ''  # Resulting message after processing

    # Process each character in the input message
    for char in message.lower():
        # If the character is not a letter, leave it unchanged
        if not char.isalpha():
            final_message += char
        else:        
            # Pick the corresponding character from the key
            key_char = key[key_index % len(key)]
            key_index += 1

            # Find the shift (offset) based on the key character
            offset = alphabet.index(key_char)
            # Find the position of the current message character
            index = alphabet.find(char)

            # Compute the new shifted index (encryption or decryption)
            new_index = (index + offset * direction) % len(alphabet)

            # Append the shifted character to the final message
            final_message += alphabet[new_index]
    
    return final_message


def encrypt(message, key):
    """Encrypt the given message using the Vigenère cipher."""
    return vigenere(message, key)
    

def decrypt(message, key):
    """Decrypt the given message using the Vigenère cipher."""
    return vigenere(message, key, -1)


# --- Program execution ---

# Print the encrypted text
print(f'\nEncrypted text: {text}')
# Print the custom key
print(f'Key: {custom_key}')
# Decrypt the message using the key
decryption = decrypt(text, custom_key)
# Print the decrypted (original) message
print(f'\nDecrypted text: {decryption}\n')
