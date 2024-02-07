class AnagramChecker:
    def __init__(self,word_list_file):
        self.word_list=self.load_word_list(word_list_file)
    def load_word_list(self,word_list_file):
        try:
            with open(word_list_file,'r')as file:
                word_list=set(word.strip().lower() for word in file)
            return word_list
        except FileNotFoundError:
            print(f'Error:File"{word_list_file}"is not found')
            return set
        
    def is_valid_word(self,word):
        return word.lower()in self.word_list
    
    def get_anagrams(self,words):
        words=words.lower()
        sorted_word=''.join(sorted_word)

