#1
input_sequence = input("Enter a comma-separated sequence of words: ")
words = [word.strip() for word in input_sequence.split(',')]
sorted_words = sorted(words)
output_sequence = ','.join(sorted_words)
print("Sorted Output:", output_sequence)

#2
def longest_word(sentence):
    words = sentence.split()
    word_lengths = [len(word.strip('.,\'"?!')) for word in words]
    max_length_index = word_lengths.index(max(word_lengths))
    return words[max_length_index]

print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever."))  
print(longest_word("Forgetfulness is by all means powerless!")) 