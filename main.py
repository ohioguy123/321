import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("""
    \033[1;37;40m▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄     
    \033[1;37;40m▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌  ▄█░░░░▌    
     \033[1;37;40m▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌ ▐░░▌▐░░▌    
              \033[1;37;40m▐░▌          ▐░▌  ▀▀ ▐░░▌    
     \033[1;37;40m▄▄▄▄▄▄▄▄▄█░▌          ▐░▌     ▐░░▌    
    \033[1;37;40m▐░░░░░░░░░░░▌ ▄▄▄▄▄▄▄▄▄█░▌     ▐░░▌    
     \033[1;37;40m▀▀▀▀▀▀▀▀▀█░▌▐░░░░░░░░░░░▌     ▐░░▌    
              \033[1;37;40m▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░░▌    
     \033[1;37;40m▄▄▄▄▄▄▄▄▄█░▌\033[1;31;40m▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░░█▄▄▄ 
    \033[1;37;40m▐░░░░░░░░░░░▌\033[1;31;40m▐░░░░░░░░░░░▌\033[1;37;40m▐░░░░░░░░░░░▌
     \033[1;37;40m▀▀▀▀▀▀▀▀▀▀▀  \033[1;31;40m▀▀▀▀▀▀▀▀▀▀▀  \033[1;37;40m▀▀▀▀▀▀▀▀▀▀▀ 
                                          
    Options:
    \033[1;31;40m\033[1;37;40m1. \033[1;37;40mYour Option 1
    \033[1;31;40m2. \033[1;37;40mYour Option 2
    \033[1;31;40m\033[1;37;40m3. \033[1;32;40mYour Option 3
    \033[1;31;40m\033[1;37;40m00. Exit
    """)

def main():
    while True:
        display_menu()
        user_choice = input("Enter your choice: ")
        
        if user_choice == '1':
            print("\033[1;37;40mYou selected Option 1.")
            # Add your logic for Option 1 here
        elif user_choice == '2':
            print("\033[1;37;40mYou selected Option 2.")
            # Add your logic for Option 2 here
        elif user_choice == '3':
            print("\033[1;32;40mYou selected \033[1;37;40mOption 3.")
            # Add your logic for Option 3 here
        elif user_choice == '00':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
