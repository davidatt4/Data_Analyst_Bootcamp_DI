#1
items = input("Input comma-separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

#2
def find_longest_word(sentence):
    
    words = sentence.split()

    longest_word = ""
    max_length = 0

    
    for word in words:
        
        word_length = len(word)

        if word_length > max_length:
            longest_word = word
            max_length = word_length

    return longest_word

sentence = "This is a simple example sentence with some long words like O’Connor."
result = find_longest_word(sentence)
print("Longest word:", result)
