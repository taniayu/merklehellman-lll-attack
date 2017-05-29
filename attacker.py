import liblll
import util

def crack_ciphertext(public_key, ciphertext):
    matrix = liblll.create_matrix_from_knapsack(public_key, ciphertext)
    reduced_basis = liblll.lll_reduction(matrix)
    guess = liblll.best_vect_knapsack(reduced_basis)

    if 1 in guess:
        return util.convert_bits_to_string(''.join([str(x) for x in guess]))
