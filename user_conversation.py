def conversation():
    print("Welcome to my conversation.")
    print("Do you like coding?")

    answer = input("Answer yes or no\n")
    if answer == "yes":
        print("That's good")
    elif answer.lower() == "no":
        print("Oh really?")
    else:
        print("That's too bad!!")
    print("Thanks for talking with me.")

def main() :
    conversation()
    
if __name__ == "__main__":
    main()