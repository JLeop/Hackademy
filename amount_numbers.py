def amount_numbers(a,b,c):
    counter = 0
    for i in range(a,b+1):
        if i%c == 0:
            counter = counter +1
    print(counter)
    return counter

if __name__ == "__main__":
    amount_numbers(1,30,5)
