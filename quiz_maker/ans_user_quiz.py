# For Answering User Input Quiz

# import libraries
import os
import random
from colorama import Fore, Style
import time

from quiz_utils import QuizUtils

# set up instance for QuizUtils
utils = QuizUtils()

# initialize and colorama and style of figlet
utils.colorama_init()
utils.figlet_init()

class AnsUserQuiz:
    def __init__(self, folder_name="result_folder"):
        self.folder_name = folder_name
        os.makedirs(folder_name, exist_ok=True)
        
    def list_avail_quizzes():
        quizzes = []
    
        for file in os.listdir("result_folder"):
            if (
                file.endswith(".txt")
                and (file != "!ReadMe.txt")
                and "sample-quiz" not in file
                and "result" not in file
            ):
                quizzes.append(file)
             
        if not quizzes:
            print(f"\n{Fore.RED}There's no quizzes created yet 💔 .")
            return None
    
        print(f"\n{Fore.MAGENTA}Saved Quiz Files 📁 :")
        for count in range(len(quizzes)):
            print(f"[{count + 1}] {quizzes[count]}")
        
        while True:
            try:
                select = int(input(f"\nEnter the assigned number of the quiz you want to take 🤸 : "))
            
                if 1 <= select <= len(quizzes):
                    return os.path.join("result_folder", quizzes[select - 1])
                else:
                    print(f"{Fore.RED}Invalid ❌ . Try Again 🔄️ .")
                
            except ValueError:
                print(f"{Fore.RED}Only enter numbers 🔢 . Try Again 🔄️ .")
