from os import system, name

def binary_conversion(decimal):
    number = 0
    decimal = input("Input binary number to convert to decimal: ")
    for a in decimal:
        number *= 2
        number += int(a)
    print("The decimal number for " + decimal + " equals " + str(number))

    
def decimal_conversion(binary):
    number = ''
    binary = int(input("Input decimal number to convert to binary: "))
    u = binary
    while (binary > 0):
            if (binary >= 64):
                number += '1'
                binary -= 64
            else:
                number+='0'
            if (binary >= 32):
                number += '1'
                binary -= 32
            else:
                number+='0'
            if (binary >= 16):
                number += '1'
                binary -= 16
            else:
                number+='0'
            if (binary >= 8):
                number += '1'
                binary -= 8
            else:
                number+='0'
            if (binary >= 4):
                number += '1'
                binary -= 4
            else:
                number+='0'            
            if (binary >= 2):
                number += '1'
                binary -= 2
            else:
                number+='0'
            if (binary >= 1):
                number += '1'
                binary -= 1
            else:
                number+='0'
            print("The binary number for " + str(u) + " equals " +number)


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    clear_screen()
    print("1. Binary -> Decimal")
    print("2. Decimal -> Binary")
    while True:
        version = input("Enter conversion type: ")
        if version == '1':
            binary_conversion(version)
        elif version == '2':
            decimal_conversion(version)
        else:
            print("This conversion type doesn't exist")
        more= input("Hit Enter to continue or q to quit: ")
        if more == 'q':
            break
        else:
            continue
    

if __name__ == "__main__":
    main()

#for this project, give a description explaining the code with a date.  


