def display_menu(item):
    print("   Menu:")
    print(item["A"])
    print(item["B"])
    print(item["C"])
    print(item["D"])
    user = input("ENTER: ")
    print("You have chosen " + user)
    

def main():
    list = {"A": "1. Grapes", "B": "2. Oranges", "C": "3. Strawberry", "D": "4. Raspberry"}
    display_menu(list)
    
#for items, values in item().items():
#   print(items+". "+ values)   

if __name__ == "__main__":
    main()