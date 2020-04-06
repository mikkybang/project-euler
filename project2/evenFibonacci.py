
def main():
    print(fib())
    print("problem2")


def fib():
    total = 0
    previous_value = 0
    current_value = 1
    temp = 0
    while current_value < 4000000:
        temp = previous_value + current_value
        if temp % 2 == 0:
            total = total + temp
        previous_value = current_value
        current_value = temp
    return total

if __name__ == "__main__":
    main()
