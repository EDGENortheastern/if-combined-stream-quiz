import random # to generate random numbers

def generate_question():
    """Return two random numbers and the correct answer."""
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    answer = num1 * num2
    return num1, num2, answer

def check_answer(user_answer, correct_answer):
    """Return True if the user's answer is correct."""
    return user_answer == correct_answer
