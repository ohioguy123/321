import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("""
    ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄     
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌  ▄█░░░░▌    
     ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌ ▐░░▌▐░░▌    
              ▐░▌          ▐░▌  ▀▀ ▐░░▌    
     ▄▄▄▄▄▄▄▄▄█░▌          ▐░▌     ▐░░▌    
    ▐░░░░░░░░░░░▌ ▄▄▄▄▄▄▄▄▄█░▌     ▐░░▌    
     ▀▀▀▀▀▀▀▀▀█░▌▐░░░░░░░░░░░▌     ▐░░▌    
              ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░░▌    
     ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░░█▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                          
    Options:
    1. Install BusWare
    00. Exit
    """)

def install_busware():
    os.system("cd && git clone https://github.com/ohioguy123/BusWare.git && 99")
    clear_screen()
    print("""
    BusWare successfully installed and executed!
    """)
    exit()

def main():
    while True:
        display_menu()
        user_choice = input("Enter your choice: ")
        
        if user_choice == '1':
            install_busware()
        elif user_choice == '00':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
