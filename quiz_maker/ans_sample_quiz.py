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