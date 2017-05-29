def encrypt(message, public_key):
    cipher = 0
    for i in range(len(message)):
        cipher += int(message[i]) * public_key[i]
    return cipher
