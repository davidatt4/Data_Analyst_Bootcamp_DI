def count_occurrences(input_string, character):
    count = 0
    for char in input_string:
        if char == character:
            count += 1
    return count
string1 = "Programming is cool!"
char1 = "o"
result1 = count_occurrences(string1, char1)
print(f"String: {string1}\nCharacter: {char1}\nOccurrences: {result1}\n")
string2 = "This is a great example"
char2 = "y"
result2 = count_occurrences(string2, char2)
print(f"String: {string2}\nCharacter: {char2}\nOccurrences: {result2}")
