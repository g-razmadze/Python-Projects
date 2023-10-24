"""Capitals Quiz!

   Author: Giorgi Razmadze
   Date: October 24, 2023

   This is one of my projects
"""


# importing libraries
import random


# defining functions, constans and classes
def shuffle_answers(question: dict) -> list:
    """
     Shuffle the answers of a given question and return a new list.

    Args:
        question (dict): A dictionary representing a question with the following keys:

    Returns:
        list: A new list of shuffled answers.
    """
    shuffled_answers = question['answers'][:]
    random.shuffle(shuffled_answers)
    return shuffled_answers


def take_quiz(questions: list, time_limit: int) -> None:
    """Take a quiz on capitals and print the final score.

    Args:
        questions (list): A list of dictionaries representing questions. Each dictionary has the same keys as in the shuffle_answers function.
        time_limit (int): The time limit for the quiz in minutes.

    Raises:
        ValueError: If the answer choice is not a valid option number.

    Return:
        None
    """
    print("Welcome to the Capitals Quiz!\n")
    print(f"You have {time_limit} minutes to complete the quiz.\n")

    total_score = sum(question['score'] for question in questions)
    current_score = 0

    for idx, question in enumerate(questions):
        shuffled_answers = shuffle_answers(question)

        print(f"{idx + 1}. {question['question']}")
        for idx, answer in enumerate(shuffled_answers):
            print(f"   {idx + 1}. {answer}")

        answer_choice = int(
            input("Choose the option number of your answer: ")) - 1

        if 0 <= answer_choice < len(shuffled_answers):
            if shuffled_answers[answer_choice] == question['answers'][question['correct_answer_index']]:
                print("Correct!\n")
                current_score += question['score']
            else:
                print("Incorrect!\n")
        else:
            print("Invalid answer choice.\n")

    print(f"Your final score is: {current_score} out of {total_score}")


questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer_index": 0,
        "score": 10
    },
    {
        "question": "What is the capital of Georgia?",
        "answers": ["Praia", "Tbilisi", "Sofia", "Tallinn"],
        "correct_answer_index": 1,
        "score": 10
    },
    {
        "question": "What is the capital of Canada?",
        "answers": ["Doha", "Quebec City", "Ottawa", "Oslo"],
        "correct_answer_index": 2,
        "score": 10
    },
    {
        "question": "What is the capital of Australia?",
        "answers": ["Ulaanbaatar", "Sydney", "Toronto", "Canberra"],
        "correct_answer_index": 3,
        "score": 10
    },
    {
        "question": "What is the capital of Malta?",
        "answers": ["Valletta", "Rabat", "Rome", "Kabul"],
        "correct_answer_index": 0,
        "score": 10
    },
    {
        "question": "What is the capital of Morocco?",
        "answers": ["Podgorica", "Rabat", "Baku", "Minsk"],
        "correct_answer_index": 1,
        "score": 10
    },
    {
        "question": "What is the capital of Malaysia?",
        "answers": ["Ulaanbaatar", "Naypyidaw", "Kathmandu", "Kuala Lumpur"],
        "correct_answer_index": 3,
        "score": 10
    },
    {
        "question": "What is the capital of Serbia?",
        "answers": ["Belgrade", "Copenhagen", "Bratislava", "Ljubljana"],
        "correct_answer_index": 0,
        "score": 10
    },
    {
        "question": "What is the capital of Ethiopia?",
        "answers": ["Quito", "Addis Ababa", "Tallinn", "Suva"],
        "correct_answer_index": 1,
        "score": 10
    },
    {
        "question": "What is the capital of Sweden?",
        "answers": ["Stockholm", "Athens", "Budapest", "Reykjavik"],
        "correct_answer_index": 0,
        "score": 10
    }]

time_limit = 10  # in minutes


def main():
    """Main Function"""

    take_quiz(questions, time_limit)


if __name__ == "__main__":
    main()
