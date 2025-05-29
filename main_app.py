# Main Quiz App Program

# import libraries and code files
import os
import time
from pyfiglet import Figlet
from colorama import Fore, Back, Style, init

from sample_quiz import run_prequiz, sample_ques
from user_quiz import input_user_quiz
from answer_user_quiz import answer_selected_quiz

# initialize colorama
init(autoreset=True)

# function for clearing screen 
def clear_content():
    os.system('cls' if os.name == "nt" else "clear")

# Inserts ASCII art for title
test = Figlet(font='elite')
clear_content() 
print(Fore.YELLOW + test.renderText('~ Quiz Master ~'))
time.sleep(1)

# enter username
username = input("\n\nHi! Enter your username 👾 : ")
clear_content()

# Loop for the controls
while True: 
    clear_content()
    print(Fore.YELLOW + test.renderText('~ Quiz Master ~'))
    print(f"\n\n{Fore.WHITE}Welcome to Quiz Master ✨, {Fore.GREEN + username}{Fore.WHITE}! Let's get started 🔥")
    print(f"\n{Fore.YELLOW}What would you like to do? 🤸")
    print(f"{Fore.CYAN}   [1] 📝 Create Quiz (10 Questions)")
    print(f"{Fore.CYAN}   [2] 🧩 Take Sample Quiz (Random 5 Items Science Quiz)")
    print(f"{Fore.CYAN}   [3] 🏅 Answer Your Created Quiz")
    print(f"{Fore.RED}   [4] 😭 Exit")

    selected = input(f"{Fore.GREEN}Select an option (1-4): ")
    
    if selected == "1":
        clear_content()
        print(Fore.CYAN + test.renderText('~ Quiz Master ~'))
        input_user_quiz()
        input(f"\n\n{Back.CYAN + Style.DIM}Press Enter to return to Main Menu 🤸 ...{Style.RESET_ALL}")
        clear_content()
    
    elif selected == "2":
        clear_content()
        print(Fore.CYAN + test.renderText('~ Quiz Master ~'))
        run_prequiz(sample_ques)
        input(f"\n\n{Back.CYAN + Style.DIM}Press Enter to return to Main Menu 🤸 ...{Style.RESET_ALL}")
        clear_content()
        
    elif selected == "3":
        clear_content()
        print(Fore.CYAN + test.renderText('~ Quiz Master ~'))
        answer_selected_quiz()
        input(f"\n\n{Back.CYAN + Style.DIM}Press Enter to return to Main Menu 🤸 ...{Style.RESET_ALL}")
        clear_content()
    
    elif selected == "4":
        print(f"\n\n{Fore.YELLOW}Aww! Thank you for playing, see you soon {Fore.GREEN + username}!")
        break
    
    else:
        print(f"{Fore.RED}Invalid! Only select from 1-4. Kindly try again.")
        time.sleep(0.5)
        clear_content()