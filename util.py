from random import randint
from fractions import gcd
import binascii

next_int_range = 100000

def convert_string_to_bits(text):
    pattern = '0' + str(len(text) * 8) + 'b'
    return format(int(binascii.hexlify(text), 16), pattern)

def convert_bits_to_string(bits):
    return binascii.unhexlify('%x' % int('0b' + bits, 2))

def generate_keys(n):
    (private_key, key_sum) = generate_superincreasing_sequence(n)
    q = randint(key_sum + 1, key_sum + next_int_range + 1)
    r = generate_coprime(q)
    public_key = []
    for i in range(n):
        public_key.append(r * private_key[i] % q)
    return (private_key, public_key, q, r)

def generate_superincreasing_sequence(n):
    sequence = []
    prev_sum = 0
    for i in range(n):
        next_int = randint(prev_sum + 1, prev_sum + next_int_range + 1)
        sequence.append(next_int)
        prev_sum += next_int
    return (sequence, prev_sum)

def generate_coprime(q):
    gcd_found = False
    r = 1
    while not gcd_found:
        r = randint(2, q)
        gcd_found = gcd(r, q) == 1
    return r

def find_modular_inverse(r, q):
    g, t, _ = egcd(r, q)
    if g == 1:
        return t % q

def egcd(a, b):
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    while b != 0:
        z, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - z * x1
        y0, y1 = y1, y0 - z * y1
    return a, x0, y0

def solve_superincreasing_knapsack(sequence, target):
    s = target
    subset = []
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] <= s:
            subset.append('1')
            s -= sequence[i]
        else:
            subset.append('0')
    if s == 0:
        return ''.join(subset[::-1])
    return None
