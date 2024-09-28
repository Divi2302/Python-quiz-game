import sys
def ask_question(question, options, correct_option, score_increment):
    """Function to ask a quiz question and return updated score or end the game if incorrect."""
    print(question)
    for option in options:
        print(option)
    

    try:
        user_answer = int(input("Enter your option (1, 2, 3, or 4): "))
        if user_answer == correct_option:
            return score_increment, True  # Return points and True for correct answer
        else:
            print("Oops! You lost. Try again next time.")
            return 0, False  # Game ends if answer is incorrect
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return 0, False  # Handle non-numeric input

def quiz_game():
    """Main function to run the quiz game."""
    name = input("Enter your name: ")
    print(f"Welcome to the Basic Python Quiz, {name}!")

    print('''\nRules to follow throughout the game:
    1. There will be 10 questions in the quiz.
    2. You will get money as a score and can only win if all the questions are answered correctly.
    3. If you answer a question incorrectly, you will lose all the money.
    4. You have to answer by entering the option number (1, 2, 3, or 4).
    5. Whenever feel like quitting the game,you can enter q in spite of answer''')

    agree = input("Enter 'y' if you agree to the rules: ").lower()
    
    if agree != "y"or "Y":
        print("You didn't agree to the rules. Exiting the game.")
        return

    print("Let's start the game!")

    # Initialize score
    score = 0

    # List of questions, options, correct answers, and score increments
    questions =  [("Who developed Python Programming Language?", 
         ["1. Wick Van Rossum", "2. Rasmus Lerdof", "3. Guido Van Rossum", "4. Niene Stom"], 3, 10),
        
        ("Which type of programming does Python support?", 
         ["1. Object-oriented", "2. Structured", "3. Functional", "4. All of the above"], 4, 50),
        
        ("What will be the value of the following Python expression (4 + 3 % 5)?", 
         ["1. 7", "2. 4", "3. 2", "4. 1"], 1, 100),
        
        ("Which of the following is used to define a block of code in Python?", 
         ["1. Key", "2. Indentation", "3. Brackets", "4. All of these"], 2, 250),
        
        ("Which keyword is used for functions in Python?", 
         ["1. Function", "2. def", "3. func", "4. Define"], 2, 500),

         ("What will be the output of this python code:\n i=1\n while True:\n if i%3==0:\n break;\n print(i)\n i+=1",
         ["1. 1 2 3", "2. error", "3. 1 2", "4. none of the above"],3,800),

         ("which of the following functions can help us to find the version of python we are currently working on?", 
           ["1. sys.version(1)", "2. sys.version(0)", "3. sys.version()", "4. sys.version"],4,1200),

        ("Python supports the creation of anonymous function at runtime,using a construct called,______",
         ["1. pi", "2. anonymous" ,"3. lambda", "4.none of the above"],3,1650),


         ("What will be the output of the following python function?\n min(max(False, -3, -4), 2, 7)",
            ["1. -4", "2. -3", "3. 2", "4. False"],4,2800)]

    # Loop through questions
    for question, options, correct_option, score_increment in questions:
        print(f"\nCurrent score: {score} Rs")
        new_points, correct = ask_question(question, options, correct_option, score_increment)
        if correct:
            score += new_points
        else:
            print(f"Game over! You lost with a total score of {score} Rs.")
            return

    # If all questions are answered correctly
    print(f"\nCongratulations {name}! You completed the quiz with a total score of {score} Rs.")

    
    answer = input(f"{question} (Type 'q' to quit): ").strip().lower()
    if answer == 'q':
        print("You chose to quit the game. Goodbye!")
        sys.exit()  # Exits the program


# Running the refactored quiz game
quiz_game()

