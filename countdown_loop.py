def while_counter(num):
    while (num >= 0):
        print(num)
        num -= 1
    

def for_counter(num):
    for num in range (10, -1, -1):
        print(num)
        

def main():
    counter = 10
    while_counter(counter)
    for_counter(counter)


if __name__ == "__main__":
    main()