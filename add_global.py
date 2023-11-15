def add():
    Var = 42
    num = int(input("Insert number between 1 and 9: "))
    if num >= 1 and num <= 9:
        return(True, num + Var)
    else:
        print("Invalid number!!")
        return(False, None)
        

def main():
    check = False
    while not check:
        check, number = add()
    print("Sum:", number ,"is a whole number")

if __name__ == "__main__":
    main()