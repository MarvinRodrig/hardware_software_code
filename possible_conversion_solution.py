


# this is incomplete




from os import system, name

def clear_screen():
# this function clears the screen only when the code is run by the user
# this function also requires this "from os import system, name" code to be imported to use this function
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def get_menu(): 
    menu_dict = {'1': 'binary->decimal', '2': 'decimal->binary', 'x':'exit_program'}
    return menu_dict

def display_menu():
    menu_dict = get_menu()

    for items, values in menu_dict.items():
        print(items+"."+ values.replace('_',' '))

def main():
    clear_screen()
    menu_selection = display_menu()

if __name__ == "__main__":
    main()