class text():
    
    def __init__(self, text):
        self.text=text

    def word_frequency(self, word):
        words=self.text.split()
        count=words.count
        return count
    
    def most_common_word(self):
     words = self.text.split()
     if not words:
        return None       
     word_counts = {}
     for word in words:
        if word in word_counts:
                word_counts[word] += 1
        else:
                word_counts[word] = 1
        
     max_count = 0
     most_common = None
     for word, count in word_counts.items():
         if count > max_count:
                max_count = count
                most_common = word
     return most_common
    
    def unique_words(self):
     words = self.text.split()
     unique = []
     seen = set()
     for word in words:
        if word not in seen:
            seen.add(word)
            unique.append(word)
     return unique
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return cls(content)
 