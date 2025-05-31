import os
from colorama import init
from pyfiglet import Figlet

class LibraryHelpers:
    def clear_content(self):
        os.system('cls' if os.name == "nt" else "clear")
        
    def colorama_init(self):
        init(autoreset=True)
    
    def figlet_init(self):
        self.test = Figlet(font='elite')
        