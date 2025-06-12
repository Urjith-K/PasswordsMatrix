# passwords_matrix.py

import numpy as np
import string

def to_ascii_matrix(word):
    ascii_vals = [ord(c) for c in word]
    matrix = np.array(ascii_vals).reshape(3, 3)
    return matrix

def calc_determinant(matrix):
    return int(round(np.linalg.det(matrix)))

def determinant_to_password(det, substitution_map):
    det_str = str(abs(det))
    password = ''
    for ch in det_str:
        password += substitution_map.get(ch, ch)
    return password

def generate_password(word, substitution_map=None, prefix='', suffix=''):
    if len(word) != 9:
        raise ValueError("Input must be exactly 9 characters.")

    if substitution_map is None:
        substitution_map = {
            '1': '!',
            '2': '%',
            '3': '#',
            '4': '&',
            '5': '@',
            '6': '*',
            '7': '+',
            '8': '=',
            '9': '$',
            '0': '?' 
        }

    matrix = to_ascii_matrix(word)
    det = calc_determinant(matrix)
    core_pass = determinant_to_password(det, substitution_map)
    return f"{prefix}{core_pass}{suffix}"

def interactive():
    print("Welcome to PasswordsMatrix Generator 🧩")
    word = input("Enter a 9-letter word or name: ")
    if len(word) != 9:
        print("Please enter exactly 9 characters.")
        return

    print("\nChoose substitution for digits (leave blank to use defaults):")
    substitution_map = {}
    for digit in '0123456789':
        val = input(f"Replace '{digit}' with: ")
        if val:
            substitution_map[digit] = val

    if not substitution_map:
        substitution_map = None  # use default

    prefix = input("Add a 2-3 character memory prefix (optional): ")
    suffix = input("Add a small suffix like a team or code (optional): ")

    try:
        password = generate_password(word, substitution_map, prefix, suffix)
        print(f"\nYour strong password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    interactive()
