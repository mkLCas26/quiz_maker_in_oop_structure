# Main Quiz Logic (for user-made quiz)

# import libraries
import os
from colorama import Fore, Style
import time

from quiz_maker.quiz_utils import QuizUtils
from file_organizer.quiz_data_organizer import QuizDataOrganizer

# set up instance for QuizUtils
utils = QuizUtils()

# initialize and colorama
utils.colorama_init()

# class for quiz questions
class UseQuestions:
    def __init__(self, prompt, choices, correct):
        self.prompt = prompt
        self.choices = choices
        self.correct = correct
        
class UserQuizCreator:
    def __init__(self):
        self.file_manager = QuizDataOrganizer()
    
    def input_user_quiz(self):
        user_question = []
        choices_list = []
        correct_ans = []
        choices_choose = "ABCD"
    
        print(f"{Fore.GREEN}🔥🔥🔥 LET'S MAKE A 10 ITEM QUIZ! 🔥🔥🔥\n")
    
        username = input("Enter your username again: ")
        title = input("Enter the title of your quiz (Ex: Friendship): ")
    
        for number in range(1, 11):
            print(f"\n{Fore.YELLOW}--------------------")
            questions = input(f"\nEnter Question {number}: ")
            user_question.append(questions)
        
            for letter in range(4):
                choices = input(f"  Enter Choice {chr(65 + letter)}: ")
                choices_list.append(choices)
            
            while True:
                correct_choice = input(f"\n{Fore.CYAN}What is the correct answer for this question? ").upper()
                if correct_choice not in choices_choose:
                    print(f"{Fore.RED}'{Fore.WHITE + correct_choice}{Fore.RED}' is invalid ❌ . {Fore.GREEN}Only choose between A, B, C, and D 🔄️ .")
                else:
                    correct_ans.append(correct_choice)
                    break
        
        quiz_num = self.file_manager.quiz_count_number(title)
        file_path = self.file_manager.write_user_quiz(username, title, user_question, choices_list, correct_ans, quiz_num)
        
        while True:
            edit_notice = input("\nDo you wish to edit this file right now 💭 ? [Y/N]: ").upper().strip()
    
            if edit_notice == "Y":
                os.system(f'notepad "{file_path}"')
                input(f"{Fore.BLUE}Press Enter once you're done editing... 🤸")
                break
        
            elif edit_notice == "N":
                print(f"{Fore.GREEN}Okay! File saved without further edits made 🎉 .")
                break
        
            else:
                print(f"{Fore.RED}Invalid. Enter 'Y' for Yes and 'N' for No. Try Again!")

if __name__ == "__main__":
    quiz_creator = UserQuizCreator()
    quiz_creator.input_user_quiz()