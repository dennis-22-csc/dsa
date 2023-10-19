x = 0
def print_num(n):
    global x
    if n > 0:
        x += 1
        return print_num(n-1) + x
    return 0

print("Result: ", print_num(10))
