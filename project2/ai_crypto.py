import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

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

def decrypt_file(input_path: str, output_path: str, key: bytes) -> None:
    """
    Decrypts an AES-256-GCM encrypted file.
    
    :param input_path: Path to the encrypted file.
    :param output_path: Path where the decrypted file will be saved.
    :param key: The 32-byte (256-bit) encryption key used during encryption.
    """
    aesgcm = AESGCM(key)
    
    # Read the contents of the encrypted file
    with open(input_path, "rb") as f:
        file_data = f.read()
        
    # Separate the 12-byte nonce from the rest of the ciphertext
    nonce = file_data[:12]
    ciphertext = file_data[12:]
    
    try:
        # Decrypt the data (this also validates the authentication tag)
        plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data=None)
    except InvalidTag:
        print("Error: Decryption failed! The key is incorrect or the file has been tampered with.")
        return
        
    # Write the recovered plaintext to the output file
    with open(output_path, "wb") as f:
        f.write(plaintext)
        
    print(f"File successfully decrypted: {output_path}")

# Example usage:
key = AESGCM.generate_key(bit_length=256)
encrypt_file("secret.txt", "secret.txt.enc", key)
decrypt_file("secret.txt.enc", "secret_recovered.txt", key)
