import re
from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        word_count = Counter(re.findall(r'\b\w+\b', self.text.lower()))
        return word_count.get(word, 0)

    def most_common_word(self):
        words = re.findall(r'\b\w+\b', self.text.lower())
        word_count = Counter(words)
        return word_count.most_common(1)[0][0] if word_count else None

    def unique_words(self):
        return list(set(re.findall(r'\b\w+\b', self.text.lower())))

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        return cls(text)


text_example = "A good book would sometimes cost as much as a good house."
text_instance = Text(text_example)
print(f"Word frequency of 'good': {text_instance.word_frequency('good')}")
print(f"Most common word: {text_instance.most_common_word()}")
print(f"Unique words: {text_instance.unique_words()}")
text_from_file = Text.from_file('the_stranger.txt')
print(f"Word frequency of 'the': {text_from_file.word_frequency('the')}")
print(f"Most common word: {text_from_file.most_common_word()}")
print(f"Unique words: {text_from_file.unique_words()}")
