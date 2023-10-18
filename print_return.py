def print_meters_to_cm(meters) :
    print(meters * 100)

def return_meters_to_cm(meters) :
    return 100 * meters    

def main() :
    return_cm = return_meters_to_cm(1)
    print_cm = print_meters_to_cm(1)

if __name__ == "__main__":
    main()