def binary_conversion(decimal):
    decimal = "bread"
    print(decimal)
    

def decimal_conversion(binary):
    binary = "toast"
    print(binary)
    


def main():
    print("1. Binary -> Decimal")
    print("2. Decimal -> Binary")
    version = input("Enter conversion type:")
    if version == 1:
        binary_conversion(version)
    elif version == 2:
        decimal_conversion(version)
        

        

if __name__ == "__main__":
    main()