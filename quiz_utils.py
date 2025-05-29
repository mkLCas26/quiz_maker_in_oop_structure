import os
import colorama
import from pyfiglet import Figlet

class QuizUtils:
    def clear_content():
        os.system('cls' if os.name == "nt" else "clear")
        