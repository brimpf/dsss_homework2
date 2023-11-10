import random


def rand_int(min, max):
    """
    Returns a random Integer in range[min, max] including the bounds
    :param min: first bound
    :param max: second bound
    :return: int
    """
    return random.randint(min, max)


def rand_op():
    """
    Returns a random operator out of (+, -, *)
    :return: string
    """
    return random.choice(['+', '-', '*'])


def calculate(first_number, second_number, operator):
    """
    Takes two numbers and a mathematical operator,
    Returns the formula and result thereof
    :param first_number: random number
    :param second_number: random number
    :param operator: '+', '-', '*'
    :return: string, int
    """
    # the problem is formulated
    problem = f"{first_number} {operator} {second_number}"

    # calculating the correct answer
    if operator == '+':
        answer = first_number + second_number
    elif operator == '-':
        answer = first_number - second_number
    else:
        answer = first_number * second_number
    return problem, answer


def math_quiz():
    """
    Creates a preset number of random math questions for the user,
    checks the user answers and calculates a score accordingly
    :return:
    """

    score = 0  # score starts at 0 and can be a maximum equal to number_of_questions
    number_of_questions = 3  # the number of questions asked in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_of_questions):

        # initializing the random values and operator for the problem
        first_number = rand_int(1, 10)
        second_number = rand_int(1, 5)
        operator = rand_op()

        # the problem and answer are calculated
        problem, answer = calculate(first_number, second_number, operator)
        print(f"\nQuestion: {problem}")

        user_answer = input("Your answer: ")

        # error handling for wrong user inputs
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("The input was not valid")

        # user input is evaluated and either the score is updated or the correct answer is provided
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{number_of_questions}")


if __name__ == "__main__":
    math_quiz()
