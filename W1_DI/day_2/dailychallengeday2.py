#Daily Challenge
num=int(input("Give me a number:"))
len=int(input("Give me a length:"))

multiplication=[num*i for i in range(1,len+1)]
print(f"List of multiplication of {num}up to{len}:")
print(multiplication)


#2
def remove_consecutive_duplicates(input_string):
    result = ""
    prev_char = ""

    for char in input_string:
        if char != prev_char:
            result += char
        prev_char = char

    return result
user_input = input("Enter a string: ")
result_string = remove_consecutive_duplicates(user_input)
print("New word:", result_string)

