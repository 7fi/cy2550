import bcrypt

def hash_password(password: str) -> str:
    """Return a secure hash of password suitable for database storage."""
    encodedPW = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(encodedPW, salt)
    return hash.decode('utf-8')

def verify_password(password: str, stored_hash: str) -> bool:
    """Return True if password matches stored_hash, False otherwise."""
    encodedPW = password.encode('utf-8')
    encodedHash = stored_hash.encode('utf-8')
    return bcrypt.checkpw(encodedPW, encodedHash)