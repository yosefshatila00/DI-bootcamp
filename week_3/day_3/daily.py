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
    def from_file(cls, words):
        with open(words, 'r', encoding='utf-8') as file:
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


if __name__ == "__main__":
    print("=== Text Analysis Demonstration ===\n")
    
    print("1. Analyzing a Simple String:")
    sample_text = "Hello, world! Hello there. World, hello! How are you today?"
    text_obj = Text(sample_text)
    
    print(f"Original text: {sample_text}")
    print(f"Frequency of 'Hello': {text_obj.word_frequency('Hello')}")
    print(f"Frequency of 'world': {text_obj.word_frequency('world')}")
    print(f"Most common word: {text_obj.most_common_word()}")
    print(f"Unique words: {text_obj.unique_words()}")
    print()
    
    print("2. Analyzing Text from a File:")
    try:
        with open('sample_text.txt', 'w', encoding='utf-8') as f:
            f.write("This is a sample text file.\nIt contains multiple lines of text.\nText analysis is fun!")
        
        file_text = Text.from_file('sample_text.txt')
        print(f"File content: {file_text.text}")
        print(f"Most common word in file: {file_text.most_common_word()}")
        print(f"Unique words in file: {file_text.unique_words()}")
    except Exception as e:
        print(f"File error: {e}")
    print()
    
    print("3. Text Modification:")
    mod_text = TextModification(sample_text)
    
    no_punct = mod_text.remove_punctuation()
    print(f"Without punctuation: {no_punct.text}")
    
    no_stop = mod_text.remove_stop_words()
    print(f"Without stop words: {no_stop.text}")
    
    no_special = mod_text.remove_special_characters()
    print(f"Without special characters: {no_special.text}")
    
    cleaned = (mod_text.remove_punctuation()
                         .remove_stop_words()
                         .remove_special_characters())
    print(f"Fully cleaned text: {cleaned.text}")
    print(f"Most common word (cleaned): {cleaned.most_common_word()}")
    print(f"Unique words (cleaned): {cleaned.unique_words()}")