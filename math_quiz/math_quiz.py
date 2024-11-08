import random
def generate_random_integer(min_val, max_val):
    """
    Generate a random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)

def generate_random_operator():
    """
    Choose a random mathematical operator from +, -, *.
    """
    return random.choice(['+', '-', '*'])

def calculate_expression(num1, num2, operator):
    """
    Calculate the result of an expression and prepare the question as a string.
    
    Parameters:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The mathematical operator (+, -, *).
        
    Returns:
        tuple: A tuple containing the formatted problem (str) and the answer (int).
    """
    expression = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return expression, answer

def math_quiz():
    """
    Runs a math quiz with a set number of random math questions. The player
    inputs their answer, which is checked and scored accordingly.
    """
    score = 0
    total_questions = 5  # Set total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator for the question
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # Changed 5.5 to 5 to keep it an integer
        operator = generate_random_operator()

        # Prepare the problem and its correct answer
        problem, correct_answer = calculate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Attempt to capture and validate user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
