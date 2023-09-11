def c_print(text):
    with open('stdout', 'a') as file:
        file.write(f"{text}\n")

prices = [30, 10, 40, 70, 60]
prices_dict = {}
for i in range(len(prices)):
    complement = 100 - prices[i]
    prices_dict[prices[i]] = i
    if complement in prices_dict:
        print(f"{i} and {prices_dict[complement]}")
