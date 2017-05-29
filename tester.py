import time
from random import choice
import string
import util
from encryption import *
from decryption import *
from attacker import *

def test_decryption(text):
    message = util.convert_string_to_bits(text)
    n = len(message)
    private_key, public_key, q, r = util.generate_keys(n)
    cipher = encrypt(message, public_key)
    decrypted_text = decrypt(cipher, public_key, private_key, q, r)
    success = decrypted_text == text
    return success

def test_attack(text):
    message = util.convert_string_to_bits(text)
    n = len(message)
    private_key, public_key, q, r = util.generate_keys(n)
    cipher = encrypt(message, public_key)
    cracked = crack_ciphertext(public_key, cipher)
    success = cracked == text
##    print success
    return success

num_tests = 100
accuracy = {}
runtime = {}
chars = string.ascii_letters + string.digits + string.punctuation
for l in range(2, 11):
    correct = 0
    start = time.time()
    for i in range(num_tests):
        random_text = ""
        for n in range(l):
            random_text += choice(chars)
        if test_attack(random_text):
            correct += 1
    end = time.time()
    accuracy[l] = correct / float(num_tests)
    runtime[l] = end - start
    print accuracy[l]
    print runtime[l]
