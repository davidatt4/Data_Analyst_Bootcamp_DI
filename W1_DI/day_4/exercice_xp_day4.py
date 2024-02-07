#1
def display_message():
    "Display a message about what I am learning"
    
msg="I am learning to code with python language"
print(msg)

#2
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print('One of my favorite books is'+title)

favorite_book('The Abstract Wild')
#3
def describe_city(city, country='france'):
    """Describe a city in a country"""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Marseille')
describe_city("Paris")

#4
import random
rn1=random.randint(1,100)
nr2=random.randint(1,100)
if rn1==nr2:
    print(f'Wow you are lucky today!')
else:
    print(f'Not lucky today')
print(rn1,nr2)

#5
def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the text is '{message}'.")

def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")

make_shirt()  
make_shirt(size="Medium")  
make_shirt(size="Small", text="Python is awesome!")  

#6
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)


#7
import random

def get_random_temp(season):
    """
    Generate a random temperature based on the given season.

    Parameters:
    - season (str): The season for which the temperature should be generated.

    Returns:
    - float: A random temperature within the specified range for the given season.
    """
    temperature_ranges = {
        'winter': (-10, 16),
        'spring': (0, 23),
        'summer': (24, 40),
        'autumn': (0, 16),
    }

    if season.lower() not in temperature_ranges:
        raise ValueError("Invalid season. Please choose from 'winter', 'spring', 'summer', or 'autumn'.")

    lower_limit, upper_limit = temperature_ranges[season.lower()]
    return round(random.uniform(lower_limit, upper_limit), 1)

def main():
    user_input = input("Enter the season ('winter', 'spring', 'summer', 'autumn') or the month number (1-12): ")
    if user_input.isdigit():
        month = int(user_input)
        if 1 <= month <= 3:
            season = 'winter'
        elif 4 <= month <= 6:
            season = 'spring'
        elif 7 <= month <= 9:
            season = 'summer'
        else:
            season = 'autumn'
    else:
        season = user_input.lower()
    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temperature <= 23:
        print("The weather is mild. Enjoy your day!")
    elif 24 <= temperature <= 32:
        print("It's warm outside. Stay cool!")
    else:
        print("It's hot! Stay hydrated and find some shade.")
main()
#8
import random
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def quiz():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    random.shuffle(data)  
    for question_data in data:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        user_answer = input(f"{question}: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
            incorrect_answers += 1
            wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

    display_results(correct_answers, incorrect_answers, wrong_answers)

def display_results(correct, incorrect, wrong_answers):
    print("\n=== Quiz Results ===")
    print(f"Correct Answers: {correct}")
    print(f"Incorrect Answers: {incorrect}")

    if incorrect > 3:
        print("\nYou had more than 3 wrong answers. Would you like to play again?")
        play_again = input("Enter 'yes' to play again, or any other key to exit: ").lower()
        if play_again == 'yes':
            quiz()
        else:
            print("Thanks for playing!")

    if wrong_answers:
        print("\n=== Wrong Answers ===")
        for wrong_answer in wrong_answers:
            print(f"Question: {wrong_answer['question']}")
            print(f"Your Answer: {wrong_answer['user_answer']}")
            print(f"Correct Answer: {wrong_answer['correct_answer']}\n")
quiz()
