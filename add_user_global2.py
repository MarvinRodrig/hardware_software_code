Var=42

def ask_me():
    num = int(input("Enter number:"))
    return(num)
    
def add(num):
    return(num + Var)

def main():
    n1 = ask_me()
    n1 += ask_me()
    sum = add(n1)
    print("Sum:",sum)
    print("Global:",Var)

if __name__ == "__main__":
    main()