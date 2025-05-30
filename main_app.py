# Main Quiz App Program

# import libraries and code files
import os
import time
from pyfiglet import Figlet
from colorama import Fore, Back, Style, init

from quiz_maker.quiz_utils import QuizUtils
from quiz_maker.ans_sample_quiz import AnsSampleQuiz, sample_ques
from quiz_maker.user_quiz_creator import UserQuizCreator
from quiz_maker.ans_user_quiz import AnsUserQuiz

# set up instance for QuizUtils
utils = QuizUtils()

# initialize colorama
utils.colorama_init

# Inserts ASCII art for title
utils.figlet_init()
utils.clear_content()
print(Fore.YELLOW + utils.test.renderText('~ Quiz Master ~'))
time.sleep(1)

class MainQuizApp:
    def __init__(self):
        self.username = ""
    
    def quiz_title(self, color=Fore.YELLOW):
        utils.clear_content()
        print(color + utils.test.renderText('~ Quiz Master ~'))
    
    def get_username(self):
        utils.clear_content()
        self.quiz_title()
        self.username = input("\n\nHi! Enter your username 👾 : ")
        utils.clear_content()
        
    def main_menu(self):
        while True:
            utils.clear_content()
            self.quiz_title()
            print(f"\n\n{Fore.WHITE}Welcome to Quiz Master ✨, {Fore.GREEN + self.username}{Fore.WHITE}! Let's get started 🔥")
            print(f"\n{Fore.YELLOW}What would you like to do? 🤸")
            print(f"{Fore.CYAN}   [1] 📝 Create Quiz (10 Questions)")
            print(f"{Fore.CYAN}   [2] 🧩 Take Sample Quiz (Random 5 Items Science Quiz)")
            print(f"{Fore.CYAN}   [3] 🏅 Answer Your Created Quiz")
            print(f"{Fore.RED}   [4] 😭 Exit")
            
            selected = input(f"{Fore.GREEN}Select an option (1-4): ")
            self.user_select(selected)
    
    def create_user_quiz(self):
        utils.clear_content()
        self.quiz_title(Fore.CYAN)
        create = UserQuizCreator
        create.input_user_quiz()
        input(f"\n\n{Back.CYAN + Style.DIM}Press Enter to return to Main Menu 🤸 ...{Style.RESET_ALL}")
        utils.clear_content()
        
    def answer_sample_quiz(self):
        utils.clear_content()
        self.quiz_title(Fore.CYAN)
        sample = AnsSampleQuiz
        sample.run_sample()
        input(f"\n\n{Back.CYAN + Style.DIM}Press Enter to return to Main Menu 🤸 ...{Style.RESET_ALL}")
        utils.clear_content()
        
    def answer_user_quiz(self):
        utils.clear_content()
        self.quiz_title(Fore.CYAN)
        quiz = AnsUserQuiz()
        quiz.answer_selected_quiz()
        input(f"\n\n{Back.CYAN + Style.DIM}Press Enter to return to Main Menu 🤸 ...{Style.RESET_ALL}")
        utils.clear_content()
    
    def user_select(self, option):
        if option == "1":
            self.create_user_quiz()
        elif option == "2":
            self.answer_sample_quiz()
        elif option == "3":
            self.answer_user_quiz()
        elif option == "4":
            print(f"\n\n{Fore.YELLOW}Aww! Thank you for playing, see you soon {Fore.GREEN + self.username}!")
            exit()
        else:
            print(f"{Fore.RED}Invalid! Only select from 1-4. Kindly try again.")
            time.sleep(1)
    
    def run_menu(self):
        self.get_username()
        while True:
            utils.clear_content()
            self.main_menu()
            
if __name__ == "__main__":
    app = MainQuizApp()
    app.run_menu()