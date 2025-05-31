class QuizHistoryHelpers:
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