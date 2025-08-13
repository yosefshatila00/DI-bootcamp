import os

class anagramchecker():
    def __init__(self, mini):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, mini)
        with open(file_path, 'r', encoding='utf-8') as file_obj:
            self.word_list = [word.strip() for word in file_obj.readlines()]

    def is_valid_word(self, word):
        return word.upper() in self.word_list
    

    def is_anagram(self, word1,word2):
        return sorted(word1.upper())==sorted(word2.upper())
    
    
    def get_anagrams(self, word):
        word=word.upper()
        anagrams=[]
        for w in self.word_list:
            if w !=word and self.is_anagram(word , w):
                anagrams.append(w)
        return anagrams



