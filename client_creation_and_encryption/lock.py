from cryptography.fernet import Fernet


def load_key() -> bytes:
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()


def generate_key() -> None:
    """
    Generates a key and save it into a file.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def unlock(encrypted_message) -> str:
    """
    Returns a decrypted message.  Input value can be byte or string, else nothing is returned.
    """
    key = load_key()
    f = Fernet(key)
    if type(encrypted_message) == str:
        decrypted_message = f.decrypt(bytes(encrypted_message.split('\'')[1], 'utf-8'))
        return decrypted_message.decode()
    elif type(encrypted_message) == bytes:
        decrypted_message = f.decrypt(encrypted_message)
        return decrypted_message.decode()
    else:
        return None

def lock(val) -> bytes:
    """
    Returns an encrypted value.
    """
    key = load_key()
    print(f"encrypting {val}")
    encoded_val = val.encode()
    f = Fernet(key)
    encrypted_val = f.encrypt(encoded_val)
    print(type(encrypted_val))
    return encrypted_val

def main():
    """
    Main function to only generate and save a key file.
    """
    generate_key()

if __name__ == "__main__":
    main()
