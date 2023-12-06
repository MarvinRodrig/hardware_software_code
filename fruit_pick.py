'''
def display_menu():
    menu_dict={'1':'Apples', '2':'Bananas', '3':'Cherries', 'X':'Pick your own'}
    while True:
        for items, values in menu_dict.items():
            print(items+". "+ values.capitalize())
        user = input('Enter: ')
        if (user == '1'):
            print(menu_dict['1']+'. nice choice')
            break
        elif(user=='2'):
            print(menu_dict['2']+'. nice choice')
            break
        elif(user=='3'):
            print(menu_dict['3']+'. nice choice')
            break
        elif(user == 'x'):
            del menu_dict['X']
            user1=input('What is your favorite fruit?\n')
            num=len(menu_dict.keys())+1
            menu_dict.update({str(num):user1, 'X':'Pick your own'})
            continue
        
        
def main():
    menu_dict=display_menu()
'''
    # print(list(menu_dict.items())) this help show all data kept in the dictionary
    # print(list(menu_dict)) this shows all key strings will give a value
    # print(list(menu_dict.values())) This shows all the values you can get from the keywords

def display_menu():
    menu_dict={'1':'Apples', '2':'Bananas', '3':'Cherries', 'X':'Pick your own'}
    while True:
        for items, values in menu_dict.items():
            print(items+". "+ values.capitalize())
        user = input('Enter: ')
        if (user in menu_dict):
            print(menu_dict[user]+'. nice choice')
            break
        elif(user == 'x'):
            del menu_dict['X']
            user1=input('What is your favorite fruit?\n')
            num=len(menu_dict.keys())+1
            menu_dict.update({str(num):user1, 'X':'Pick your own'})
            continue
        else:
            print("That doesn't exist")
                    
def main():
    menu_dict=display_menu()

if __name__ == "__main__":
    main()