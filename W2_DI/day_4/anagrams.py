from anagram_checker import AnagramChecker

def get_user_input():
    while True:
        user_input=input('Enter a word or type "exit" to quit:').strip
        if user_input.lower()=='exit':
            return None
        elif len(user_input.split())>1:
            print('Error:Only a single word is allowed.')
        elif not user_input.isalpha():
            print('Error: Only alphabetic characters are allowed')
        else:
            return user_input
        
def main():
    word_list_file='word_list.txt'
    anagram_checker=AnagramChecker(word_list_file)

    while True:
        user_word=get_user_input()
        if user_word is None:
            print('Exiting the program.Goodbye!')
            break

        user_word=user_word.strip()

        if anagram_checker.is_valid_word(user_word):
            anagrams=anagram_checker.get_anagrams(user_word)
            print("\nYOUR WORD:\'{}'\"".format(user_word.upper))
            print("This is a valid English word.")
            print("Anagrams for your word:",','.join(anagrams)if anagrams else None)

        else:
            print("\nYOUR WORD:\'{}'".format(user_word.upper()))
            print('This is not a valid english word')

        if __name__=='main':
            main()