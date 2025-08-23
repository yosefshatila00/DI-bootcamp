from daily import Text
import string

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
