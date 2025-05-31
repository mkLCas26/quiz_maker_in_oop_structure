import os
from colorama import Fore
from quiz_utilities.library_helpers import LibraryHelpers

# initialize colorama from quiz utils
utils = LibraryHelpers()
utils.colorama_init()

class QuizHistoryOrganizer:
        def __init__(self, folder_name="result_folder"):
            self.folder_name = folder_name
            os.makedirs(folder_name, exist_ok=True)
        
        def write_quiz_result(self, result_obj):
            filename_basis = f"{result_obj.username.replace(' ', '_').lower()}_sample-quiz"
            trial = 1
            while f"{filename_basis}_try{trial}.txt" in os.listdir(self.folder_name):
                trial += 1
            final_filename = f"{filename_basis}_try{trial}.txt"
            path = os.path.join(self.folder_name, final_filename)

            with open(path, "w") as f:
                f.write(f"Username: {result_obj.username}\n")
                f.write(f"Score: {result_obj.score}/5\n")
                f.write(f"\n---------- {result_obj.username}'s Quiz History ----------\n")
                for i, entry in enumerate(result_obj.history, 1):
                    f.write(f"\nQuestion {i}: {entry['question']}\n")
                    for j, choice in enumerate(entry['choices']):
                        f.write(f"    {chr(65 + j)}. {choice}\n")
                    f.write(f"\nYour answer: {entry['answer']}")
                    f.write(f"\nCorrect answer: {entry['correct_choice']}\n")

            print(f"\n{Fore.CYAN}Your quiz history is now accessible in the result_folder with the filename {Fore.WHITE + final_filename} 📁.") 