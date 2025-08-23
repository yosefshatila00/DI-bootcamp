import random
import json

def get_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            if file_path.endswith('.json'):
                data = json.load(file)
                return data if isinstance(data, list) else data.get('words', [])
            else:
                return file.read().split()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def get_random_sentence(length, words_list):
    if not words_list or length < 1:
        return "Cannot generate sentence."
    
    selected_words = [random.choice(words_list) for _ in range(length)]
    return " ".join(selected_words).lower()

def main():
    print("Random Sentence Generator")
    print("Enter a length between 2-20 words\n")
    
    try:
        length = int(input("Sentence length (2-20): "))
        if not (2 <= length <= 20):
            print("Error: Length must be between 2-20.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    file_path = "words.txt" 
    words = get_words_from_file(file_path)
    
    if not words:
        print("No words found in file.")
        return
    
    sentence = get_random_sentence(length, words)
    print(f"\nYour random sentence: {sentence}")

if __name__ == "__main__":
    main()