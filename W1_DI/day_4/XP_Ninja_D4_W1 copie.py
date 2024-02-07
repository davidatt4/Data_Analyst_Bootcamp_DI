#1
def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    else:
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
    return full_name
print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))

#2
def text_to_morse(text):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', ' ': ' '}
    morse_text = ' '.join(morse_code[char.upper()] for char in text)
    return morse_text

def morse_to_text(morse_code):
    morse_code_rev = {value: key for key, value in morse_code.items()}
    text = ''.join(morse_code_rev[char] for char in morse_code.split(' '))
    return text

print(text_to_morse("Hello World"))
print(morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))

#3
def box_printer(*args):
    max_length = max(len(word) for word in args)
    
    print('*' * (max_length + 4))
    
    for word in args:
        print(f'* {word.ljust(max_length)} *')
    
    print('*' * (max_length + 4))

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
#4
def insertion_sort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)
