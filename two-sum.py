def c_print(text):
    with open('stdout', 'a') as file:
        file.write(f"{text}\n")

prices = [30, 10, 40, 70, 60]

for price in prices:
    complement = 100 - price
    if complement in prices:
        print(f"{price} and {complement}")
