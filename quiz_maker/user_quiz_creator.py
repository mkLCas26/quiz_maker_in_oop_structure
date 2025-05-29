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
    
    
    