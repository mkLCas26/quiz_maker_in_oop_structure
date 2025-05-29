# Main Quiz Logic (for user-made quiz)

# import libraries
import os
from colorama import Fore, Style, init
import time

# initialize and colorama and style of figlet
init(autoreset=True)

# class for quiz questions
class UseQuestions:
    def __init__(self, prompt, choices, correct):
        self.prompt = prompt
        self.choices = choices
        self.correct = correct

# function for letting the user add questions
def input_user_quiz():
    user_question = []
    choices_list = []
    correct_ans = []
    choices_choose = "ABCD"
    
    print(f"{Fore.GREEN}🔥🔥🔥 LET'S MAKE A 10 ITEM QUIZ! 🔥🔥🔥\n")
    
    # Collect username
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
    
    # Save quiz data in a folder
    result_files = "result_folder"
    os.makedirs(result_files, exist_ok=True)                  # creates folder for the user, if existing it will not resturn error
    
    # Filename for quiz
    format_title = title.replace(" ", "_").lower()        # prepares username for the filename
    user_filename = f"{format_title}_quiz"                   # formats filename with username attached
    count_files = os.listdir(result_files)                      # checks for other files with the same filename
    
    # Allows multiple quiz inputs by user by separating files
    quiz_num = 1
    while (f"{user_filename}{quiz_num}.txt") in count_files:    # tracks if file is already in folder and adjusts filename no.
        quiz_num += 1
    
    final_filename = f"{user_filename}{quiz_num}.txt"
    file_path = os.path.join(result_files, final_filename)
    
    # Save user's questionnaire and correct answers in file
    with open(file_path, "w") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Quiz Number: {quiz_num}")
        file.write(f"\n---------- {title} Quiz ----------\n")
        
        for item in range(10):
            file.write(f"\nQuestion {item +1}: {user_question[item]}\n")                              # gets the question per index
            for letter in range(4):
                file.write(f"    {chr(65 + letter)}. {choices_list[item * 4 + letter]}\n")            # gets the 4 choices assigned to question
            file.write(f"Correct Answer: {correct_ans[item]}\n")
    print(f"\n{Fore.CYAN}Your quiz now is now accesible in the result_folder with the filename {Fore.WHITE + final_filename} 📁.")
    print(f"\n{Fore.YELLOW}--------------------")
    
    time.sleep(0.5)
    
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

        
if __name__ == "__main__":                        # only running program when called out
    input_user_quiz()
        