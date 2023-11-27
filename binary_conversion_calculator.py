def binary_conversion(decimal):
    while True:
        decimal = input("Input binary number to convert to decimal: ")
        break
    

def decimal_conversion(binary):
    while True:
        number = '00000000'
        binary = int(input("Input decimal number to convert to binary: "))
        while (binary > 0):
            if (binary >= 64):
                number += '01000000'
                binary -= 64
            elif (binary >= 32):
                number += '00100000'
                binary -= 32
            elif (binary >= 16):
                number += '00010000'
                binary -= 16
            elif (binary >= 8):
                number += '00001000'
                binary -= 8
            elif (binary >= 4):
                number += '00000100'
                binary -= 4
            elif (binary >= 2):
                number += '00000010'
                binary -= 2
            elif (binary >= 1):
                number += '00000001'
                binary -= 1
        print(number)
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

#for this project, give a description explaining the code with a date.  