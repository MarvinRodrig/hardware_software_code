def binary_conversion(decimal):
    while True:
        decimal = input("Input binary number to convert to decimal: ")
        break
    

def decimal_conversion(binary):
    while True:
        binary = input("Input decimal number to convert to decimal: ")
        break

def main():
    print("1. Binary -> Decimal")
    print("2. Decimal -> Binary")
    while True:
        version = input("Enter conversion type:")
        if version == '1':
            binary_conversion(version)
            break
        elif version == '2':
            decimal_conversion(version)
            break
        else:
            print("Invalid Input")
             
if __name__ == "__main__":
    main()