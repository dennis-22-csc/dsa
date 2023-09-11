def c_print(text):
    with open('stdout', 'a') as file:
        file.write(f"{text}\n")

prices = [30, 10, 40, 70, 60]

for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        if (prices[i] + prices[j] == 100):
            print(f"{prices[i]} and {prices[j]}")
