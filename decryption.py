from random import randint
from fractions import gcd
import util

def decrypt(cipher, public_key, private_key, q, r):
    t = util.find_modular_inverse(r, q)
    s = cipher * t % q
    message = util.solve_superincreasing_knapsack(private_key, s)
    return util.convert_bits_to_string(message)
