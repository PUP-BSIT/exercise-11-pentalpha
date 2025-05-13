from passlib.hash import pbkdf2_sha256

def hash_text():
    """ Prints the hashed text of the inputted string """
    text = input("Enter a string to hash: ")
    hashed = pbkdf2_sha256.hash(text)
    print(f"Hashed text: {hashed}")