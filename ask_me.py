def user_selection(num):
    print(num + ". Nice choice.")
    print("Want to continue?")
    
def main():
    print("Pizza or burger?")
    while True:
        user_input = input("1 for pizza or 2 for burger: ")
        if user_input == '1':
            user_input = "Pizza"
            user_selection(user_input)
        elif user_input == '2':
            user_input = "Burger"
            user_selection(user_input)
        else:
            print("Invalid Input")
        place = input("3 for no and 4 for yes: ")
        if place == '4':
            continue
        elif place == '3':
            break     
       
if __name__ == "__main__":
    main()