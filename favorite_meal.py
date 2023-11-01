def meal_test(answer):
    if answer == 1:
        print("Fried Chicken Yummy")
    elif answer == 2:
        print("Burger good choice")
    elif answer == 3:
        print("Pizza Nice")  
    else:
        print("That is not an option!")
    

def main(): 
    print("Which is your favorite meal?")
    print("1. Chicken")
    print("2. Burger")
    print("3. Pizza")
    print("Input your answer: ")
    answer = int(input())
    meal_test(answer)

if __name__ == "__main__":
    main()