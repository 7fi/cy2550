import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_file(input_path: str, output_path: str, key: bytes) -> None:
    """
    Encrypts a file using AES-256 in GCM mode.
    
    :param input_path: Path to the file you want to encrypt.
    :param output_path: Path where the encrypted file will be saved.
    :param key: A 32-byte (256-bit) encryption key.
    """
    # Initialize AESGCM with the provided key
    aesgcm = AESGCM(key)
    
    # Generate a secure random 12-byte nonce (number used once)
    nonce = os.urandom(12)
    
    # Read the original file contents in binary mode
    with open(input_path, "rb") as f:
        plaintext = f.read()
        
    # Encrypt the data
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)
    
    # Write the nonce and ciphertext together to the output file
    # (The nonce is safe to store publicly and is required for decryption)
    with open(output_path, "wb") as f:
        f.write(nonce + ciphertext)
        
    print(f"File successfully encrypted: {output_path}")

# Example usage:
# key = AESGCM.generate_key(bit_length=256)
# encrypt_file("secret.txt", "secret.txt.enc", key)
