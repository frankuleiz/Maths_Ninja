# A simple maths game to help the player improve their arithmetic prowess

import random
import math

#Collects the players info
first_name = input('What is your first name ?: ')
last_name = input('What is your last name ?: ')
age = input('How old are you?: ')

print(f"Hello {first_name} {last_name}.You are {age} years old!")

print("WELCOME TO THE MATHS GAME")

print("LEVEL 1")
# A function that generates arithmetic expressions
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])

#Swaps the values incase of subtraction if num2 is greater than num1
    if operator == '-' and num2 > num1:
        num1, num2 = num2, num1

    expression = f"{num1} {operator} {num2}"
    result = eval(expression)
    return expression, result

#Function that records the players score
def main():
    score = 0
    num_questions = 10

#validates the player's answer
    for _ in range(num_questions):
        expression, correct_answer = generate_question()

        print(f"Question: {expression}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}")
    
    print(f"Game Over! {first_name} {last_name} your score is {score}/{num_questions}")


if __name__ == "__main__":
    main()