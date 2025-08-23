import string
import re


class Text:
    
    def __init__(self, text):
        self.text = text
    
    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        return count if count > 0 else None
    
    def most_common_word(self):
        words = self.text.split()
        if not words:
            return None
        
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        
        most_common = max(word_counts, key=word_counts.get)
        return most_common
    
    def unique_words(self):
       
        words = self.text.split()
        unique_words_list = []
        seen_words = set()
        
        for word in words:
            if word not in seen_words:
                seen_words.add(word)
                unique_words_list.append(word)
        
        return unique_words_list
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        return cls(content)
        

