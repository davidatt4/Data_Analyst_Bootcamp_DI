#1
from datetime import datetime, timedelta

def display_today_and_next_holiday():
   
    today = datetime.now()
    print("Today's Date:", today.strftime("%Y-%m-%d %H:%M:%S"))

    
    upcoming_holiday_name = "New Year's Day"
    upcoming_holiday_date = datetime(today.year + 1, 1, 1)  # Assuming the next New Year's Day
    time_until_holiday = upcoming_holiday_date - today
    days, seconds = time_until_holiday.days, time_until_holiday.seconds
    hours, minutes = seconds // 3600, (seconds % 3600) // 60
    remaining_time_str = f"{days} days and {hours:02}:{minutes:02}:{seconds % 60:02} hours"

    print(f"The next holiday is {upcoming_holiday_name} in {remaining_time_str}.")


display_today_and_next_holiday()

#2
def calculate_age(seconds):
    orbital_periods = {
        'Earth': 1.0,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }

    earth_years = seconds / 31557600

    age_on_planets = {planet: earth_years / orbital_periods[planet] for planet in orbital_periods}

    return age_on_planets

age_in_seconds = 1000000000
ages_on_planets = calculate_age(age_in_seconds)
for planet, age in ages_on_planets.items():
    print(f"Age on {planet}: {age:.2f} Earth-years")
#3
import re

def return_numbers(input_string):
    numbers = re.findall(r'\d', input_string)
    result = ''.join(numbers)
    return result
input_string = 'k5k3q2g5z6x9bn'
output = return_numbers(input_string)
print("Expected output:", output)
#4
import re

def validate_name(name):

    pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'

    match = re.match(pattern, name)
    if match:
        return True
    else:
        return False
user_input = input("Enter your full name (e.g., John Doe): ")
if validate_name(user_input):
    print("Valid name!")
else:
    print("Invalid name. Please follow the format: First Last")
#5
import random
import string

def generate_password(length):
    
    digits = string.digits
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    special_characters = '!@#$%^&*()_-+=<>?/'

    length = max(6, min(30, length))

    password = [random.choice(digits),
                random.choice(lowercase_letters),
                random.choice(uppercase_letters),
                random.choice(special_characters)]

    password.extend(random.choices(digits + lowercase_letters + uppercase_letters + special_characters, k=length-4))

    random.shuffle(password)

    result_password = ''.join(password)

    return result_password

def is_valid_password(password):
    return any(char.isdigit() for char in password) and any(char.islower() for char in password) and \
           any(char.isupper() for char in password) and any(char in '!@#$%^&*()_-+=<>?/' for char in password)

def test_password_generator():
    for _ in range(100):
        length = random.randint(6, 30)
        password = generate_password(length)
        assert len(password) == length
        assert is_valid_password(password)

def main():
    while True:
        try:
            password_length = int(input("Enter the password length (between 6 and 30): "))
            if 6 <= password_length <= 30:
                break
            else:
                print("Please enter a number between 6 and 30.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    password = generate_password(password_length)
    print(f"\nYour generated password is: {password}\n\nKeep this password in a safe place!")

if __name__ == "__main__":
    test_password_generator()
    main()
