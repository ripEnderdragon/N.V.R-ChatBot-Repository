import random

def gen_pass(pass_length):
    elements = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password