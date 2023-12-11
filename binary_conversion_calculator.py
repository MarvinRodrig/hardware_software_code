# Written by: Marvin Rodriguez
# File name: binary_converstion_calculator.py
# Description: this file converts numbers from
# binary to decimal and vice versa.
# The code also checks if the user has given
# valid input through out the code.


# this is needed for the clear_screen function 
from os import system, name


def binary_conversion(decimal):
# this is where binary numbers are converted to decimal and the user inputs a binary number
    number = 0
    decimal = input("Input binary number to convert to decimal: ")
    for a in decimal:
        number *= 2
        number += int(a)
    print("The decimal number for " + decimal + " equals " + str(number))


def decimal_conversion(binary):
# this is where decimal number are converted to binary and the user inputs a decimal number 
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
# this function clears the screen only when the code is run by the user
# this function also requires this "from os import system, name" code to be imported to use this function
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# this is where the file "starts" and the code ask the user to input a conversion type and when the user
# gets their completed converted number, the code will also ask if they want to quit/continue with this code
def main():
    while True:
        clear_screen()
        print("1. Binary -> Decimal")
        print("2. Decimal -> Binary")
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
    
# this is the first lines of code that will be run first 
if __name__ == "__main__":
    main()
  


