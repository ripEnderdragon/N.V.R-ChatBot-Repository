import random
import time
library = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    pass_length = int(input("Pasword Length:"))
    password = ""

    for i in range (pass_length):
            password += random.choice(library)

    print(password)