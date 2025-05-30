# Main Quiz Logic (for user-made quiz)

# import libraries
import os
from colorama import Fore, Style
import time

from quiz_utils import QuizUtils

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
        
# class for filde handling and writing
class FileOrganizer:
    def __init__(self, folder="result_folder"):  
        self.folder = folder
        os.makedirs(self.folder, exist_ok=True)
        
    def write_user_quiz(self, username, title, user_question, choices_list, correct_ans, quiz_num):
        format_title = title.replace(" ", "_").lower()
        user_filename = f"{format_title}_quiz"
        final_filename = f"{user_filename}{quiz_num}.txt"
        file_path = os.path.join(self.folder, final_filename)   
    
        with open(file_path, "w") as file:
            file.write(f"Username: {username}\n")
            file.write(f"Quiz Number: {quiz_num}")
            file.write(f"\n---------- {title} Quiz ----------\n")
        
            for item in range(10):
                file.write(f"\nQuestion {item +1}: {user_question[item]}\n")                              
                for letter in range(4):
                    file.write(f"    {chr(65 + letter)}. {choices_list[item * 4 + letter]}\n")           
                
        return file_path
    
    def quiz_count_number(self, title):
        format_title = title.replace(" ", "_").lower()       
        user_filename = f"{format_title}_quiz"
        count_files = os.listdir(self.folder)
    
        quiz_num = 1
        while (f"{user_filename}{quiz_num}.txt") in count_files:    
            quiz_num += 1
        
        return quiz_num
    
    def open_file_in_notepad(seld, file_path):
        os.system(f'notepad "{file_path}"')
        time.sleep(0.5)

    