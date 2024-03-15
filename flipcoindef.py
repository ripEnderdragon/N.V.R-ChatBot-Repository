import random

# def flip_coin():
#     result = ""
#     flip = random.randint(0, 2)
#     if flip == 0:
#         result += "HEADS"
#     else:
#         result += "TAILS"
    
#     print(result)

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"