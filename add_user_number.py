def main():
    Var=42
    user1 = input("input a number: ")
    user2 = input("input another number: ")
    total = int(user1)+ int(user2)
    number = total + Var
    print("Sum:",number)
    print("Global:", Var)

if __name__ == "__main__":
    main()