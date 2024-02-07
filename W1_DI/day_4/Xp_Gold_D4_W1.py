#1
import datetime

def get_age(year, month, day):
    current_date = datetime.date(2023, 1, 1) 
    birth_date = datetime.date(year, month, day)
    age = (current_date - birth_date).days // 365  
    return age

def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)

    retirement_age_male = 67
    retirement_age_female = 62

    if gender == 'm' and age >= retirement_age_male:
        return True
    elif gender == 'f' and age >= retirement_age_female:
        return True
    else:
        return False
gender = input("Enter your gender (m/f): ")
dob = input("Enter your date of birth in the form yyyy/mm/dd: ")
if can_retire(gender, dob):
    print("Congratulations! You can retire.")
else:
    print("Sorry, you cannot retire yet.")


#2
def calculate_expression(X):
    X_str = str(X)

    result = X + int(X_str * 2) + int(X_str * 3) + int(X_str * 4)
    return result
X = 3
output = calculate_expression(X)
print(output)

#3
import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        throws += 1
        print(f"({dice1}, {dice2})")

        if dice1 == dice2:
            break

    return throws

def main():
    total_throws = 0
    throws_to_reach_doubles = []

    for _ in range(100):
        throws = throw_until_doubles()
        total_throws += throws
        throws_to_reach_doubles.append(throws)

    print(f"\nTotal throws: {total_throws}")
    average_throws = round(total_throws / 100, 2)
    print(f"Average throws to reach doubles: {average_throws}")

if __name__ == "__main__":
    main()
