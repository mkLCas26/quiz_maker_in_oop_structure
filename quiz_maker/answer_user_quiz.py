# For Answering User Input Quiz

# import libraries
import os
import random
from colorama import Fore, Style, init
from pyfiglet import Figlet
import time

# initialize and colorama and style of figlet
init(autoreset=True)
test = Figlet(font='elite')

# function for clearing screen
def clear_content():
    os.system('cls' if os.name == "nt" else "clear")

# function that allows user to choose a quiz file from folder
def list_avail_quizzes():
    quizzes = []
    
    # checks if result_folder contains quiz files
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
    
    # giving user a printed list of quiz files
    print(f"\n{Fore.MAGENTA}Saved Quiz Files 📁 :")
    for count in range(len(quizzes)):
        print(f"[{count + 1}] {quizzes[count]}")
     
    # allows user to select quiz file   
    while True:
        try:
            select = int(input(f"\nEnter the assigned number of the quiz you want to take 🤸 : "))
            
            if 1 <= select <= len(quizzes):
                return os.path.join("result_folder", quizzes[select - 1])
            else:
                print(f"{Fore.RED}Invalid ❌ . Try Again 🔄️ .")
                
        except ValueError:
            print(f"{Fore.RED}Only enter numbers 🔢 . Try Again 🔄️ .")

# function that loads/readies selected quiz file for answering     
def load_selected_quiz(quiz_file):
    questions = []
    with open(quiz_file, "r") as file:                                  # opens and reads quiz file selected
        lines = file.readlines()
    
    questions = []
    count = 1
    index = 0
    
    while index < len(lines):                                           # main loop for reading file lines
        start_line = lines[index].strip()
        
        if start_line.startswith(f"Question {count}: "):                         # extracts the question prompt
            prompt = start_line[len(f"Question {count}: "):].strip()
            count += 1
            index += 1
            
            choices = []                                                # for loop for extracting choices and storing it in a list
            for _ in range(4):
                line = lines[index].strip()
                
                if "." in line:
                    choices.append(line.split('.', 1)[1].strip())
                else:
                    choices.append(line)
                    
                index += 1
             
            # answer_line = lines[index].strip()                          # extracts the correct answer
            if lines[index].startswith("Correct Answer: "):
                correct_answer = lines[index].strip()[len("Correct Answer: "):].strip()
                correct = ord(correct_answer.upper()) - 65
            index += 1
            
            questions.append((prompt, choices, correct))                # stores all the question into 1 list
        
        else:
            index += 1
    return questions

# function that makes the user answer their selected quiz
def answer_selected_quiz():
    quiz_file = list_avail_quizzes()                                    # gets the filepath of selected quiz
    if quiz_file is None:
        return
    
    print(f"\nLoading your selected quiz: {Fore.BLUE + quiz_file}")                 # shuffles the 10 quetions of user
    questions = load_selected_quiz(quiz_file)
    clear_content()
    random.shuffle(questions)
      
    score = 0
    quiz_history = []
    correct_letter = ""
    
    print(Fore.MAGENTA + test.renderText('~ Quiz Master ~') + Style.RESET_ALL)
    
    username = input("\nEnter your username again: ")
    
    for number, item in enumerate(questions, 1):
        clear_content()
        
        print(Fore.MAGENTA + test.renderText('~ Quiz Master ~') + Style.RESET_ALL)
                                
        prompt = item[0]                                                # ensures the correct order of prompt, choices, and answer
        choices = item[1]
        correct_ans = item[2]
        
        print(f"\n\n{Fore.BLUE}Question {number}: {prompt}")                           # loop to print questions and choices
        for letter, choice in enumerate(choices):
            print(f"{    chr(65 + letter)}. {choice}")
            
        user_answer = (input(f"\n{Fore.CYAN}Answer (A-D): ")).upper()              # checking of user's answer
        if ord(user_answer[0]) - 65 == correct_ans:
            score += 1
            print(f"{Fore.GREEN}Correct! ✅\n")
        else:
            correct_letter = chr(65 + correct_ans )
            print(f"{Fore.RED}Incorrect ❌ . {Fore.WHITE}The correct answer is {Fore.GREEN + correct_letter}. {Fore.GREEN + choices[correct_ans]}\n")
        
        time.sleep(1)
        
        quiz_history.append({                                                # appends user's quiz history in a list
            "question": prompt,
            "choices": choices,
            "answer": user_answer,
            "correct_choice": f"{correct_letter}. {choices[correct_ans]}"  
        })

    print("--------------------")
    print(f"{Fore.YELLOW}Congratulations 🎉 ! You have scored {Fore.GREEN}{score} {Fore.YELLOW}out of {Fore.GREEN}5 questions.")  
    
    # Save user's results in a file
    result_files = "result_folder"
    os.makedirs(result_files, exist_ok=True)
    
    # Prepare username for filename
    format_username = username.replace(" ", "_").lower()
    user_filename = f"{format_username}_result"
    count_files = os.listdir(result_files)
    
    # Adds trial number in filename
    trial = 1
    while (f"{user_filename}_try{trial}.txt") in count_files:
        trial +=1
    
    final_filename = f"{user_filename}_try{trial}.txt"
    file_path = os.path.join(result_files, final_filename)
    quiz_title = os.path.basename(quiz_file)                           # extracts quiz title
    
    # Save user's quiz history in file
    with open(file_path, "w") as file:                                        # opens file and writes quiz history
        file.write(f"Username: {username}\n")
        file.write(f"Quiz Taken: {quiz_title}\n")
        file.write(f"Score: {score}/10\n")
        file.write(f"\n---------- {username}'s Quiz History ----------\n")    
        
        for number, entry in enumerate(quiz_history, 1):
            file.write(f"\nQuestion {number}: {entry['question']}\n")
            for letter, choice in enumerate(entry['choices']):
                file.write(f"    {chr(65 + letter)}. {choice}\n") 
            
            file.write(f"\nYour answer: {entry['answer']}")
            file.write(f"\nCorrect answer: {entry['correct_choice']}")
    print(f"\n{Fore.CYAN}Your quiz history is now accesible in the result_folder with the filename {Fore.WHITE + final_filename} 📁.")
            
if __name__ == "__main__":      
    answer_selected_quiz()