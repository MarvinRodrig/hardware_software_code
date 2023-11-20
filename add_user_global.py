Var=42
def ask_me():
    num = int(input("Enter number:"))
    return(num)
    
def add_global(num):
    return(num)
    
def main():
    global Var
    n1 = ask_me()
    n2 = ask_me()
    sum = add_global(n2)
    sum += add_global(n1)
    sum += add_global(Var)
    print("Sum:",sum)
    print("Global:",Var)

if __name__ == "__main__":
    main()
