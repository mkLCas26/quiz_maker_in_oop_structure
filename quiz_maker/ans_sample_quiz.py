# Main Quiz Logic (for pre-programmed 5 item quiz)

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

class SampleQuestions:
    def __init__(self, prompt, choices, correct):
        self.prompt = prompt
        self.choices = choices
        self.correct = correct
        
class QuizHistory:
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.history = []
        
    def result(self, question, user_answer, correct_index, choices):
        correct_letter = chr(65 + correct_index)
        correct_choice = f"{correct_letter}. {choices[correct_index]}"
        
        self.history.append({
            "question": question,
            "choices": choices,
            "answer": user_answer,
            "correct_choice": correct_choice
        })
        
        if user_answer and ord(user_answer[0]) - 65 == correct_index:
            self.score += 1
            return True, correct_choice
        else:
            return False, correct_choice

# list of question prompts
question_prompts = [
    "What is the largest ocean in the world?",
    "What is the deepest trench in the world?",
    "What is largest gas planet?",
    "How much of the Earth's surface is water mass?",
    "What is the second most abundant element in the Earth's atmosphere?",
    "What is Earth's highest point above sea level?",
    "How old is Earth?",
    "What plate is the fastest-moving among all of Earth's plates?",
    "What planet has the most moons/satelites?",
    "What are the Earth's four major layers?"
]

# list of questions with choices and correct answer index
sample_ques = [
    SampleQuestions(
        question_prompts[0],
        ["Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Atlantic Ocean"],
        0
    ),
    
    SampleQuestions(
        question_prompts[1],
        ["Kermadec Trench", "Tonga Trench", "Marianas Trench", "New Britain Trench"],
        2
    ),
    
    SampleQuestions(
        question_prompts[2],
        ["Saturn", "Neptune", "Uranus", "Jupiter"],
        3
    ),
    
    SampleQuestions(
        question_prompts[3],
        ["70%", "71%", "68%", "73%"],
        1
    ),
    
    SampleQuestions(
        question_prompts[4],
        ["Nitrogen", "Argon", "Carbon Dioxide", "Oxygen"],
        3
    ),
    
    SampleQuestions(
        question_prompts[5],
        ["Kangchenjunga", "Mount Ararat", "K2", "Mount Everest"],
        3
    ),
    
    SampleQuestions(
        question_prompts[6],
        ["About 4.54 billion years", "About 5 billion years", "About 4.6 billion years", "About 8.1 billion years"],
        0
    ),
    
    SampleQuestions(
        question_prompts[7],
        ["South American Plate", "North American Plate", "Pacific Plate", "African Plate"],
        2
    ),
    
    SampleQuestions(
        question_prompts[8],
        ["Earth", "Saturn", "Jupiter", "Uranus"],
        1
    ),
    
    SampleQuestions(
        question_prompts[9],
        ["Shell, Mantle, First Core, Second Core", "Crust, Mantle, Outer Core, Inner Core",
         "Cover, Mantle, Inner Core, Outer Core", "Crust, Second Layer, Contents, Specifics"],
        1
    )
]

