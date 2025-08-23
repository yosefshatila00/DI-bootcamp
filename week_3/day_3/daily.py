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
        

class TextModification(Text):
 
    
    def __init__(self, text):
        super().__init__(text)
    
    def remove_punctuation(self):
       
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = self.text.translate(translator)
        return TextModification(cleaned_text)
    
    def remove_stop_words(self, custom_stop_words=None):
    
        default_stop_words = {
            'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 
            'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 
            'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 
            'will', 'would', 'could', 'should', 'may', 'might', 'must',
            'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him',
            'her', 'us', 'them', 'this', 'that', 'these', 'those', 'my',
            'your', 'his', 'its', 'our', 'their', 'mine', 'yours', 'hers',
            'ours', 'theirs', 'myself', 'yourself', 'himself', 'herself',
            'itself', 'ourselves', 'yourselves', 'themselves'
        }
        
        stop_words = set(custom_stop_words) if custom_stop_words else default_stop_words
        
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        cleaned_text = ' '.join(filtered_words)
        
        return TextModification(cleaned_text)
    
    def remove_special_characters(self):
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        return TextModification(cleaned_text)
