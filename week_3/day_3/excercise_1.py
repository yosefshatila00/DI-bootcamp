import random
import os


def get_words_from_file(file_path):
  
    try:
        # For memory efficiency with large files, read line by line
        words = []
        with open(file_path, "r") as file:
            for line in file:
                # Split each line into words and extend the list
                words.extend(line.split())
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def get_random_sentence(length, words_list):
 
    if not words_list:
        raise ValueError("Cannot generate sentence from empty word list")
    
    if length <= 0:
        raise ValueError("Sentence length must be positive")
    
    selected_words = random.choices(words_list, k=length)
    sentence = " ".join(selected_words).lower() + "."
    return sentence

def main():
   
    print("Welcome to the Random Sentence Generator!")
    print("This program generates random sentences from a word list.")
    print("The sentence length must be between 2 and 20 words.\n")
    
    # File path - you can change this to match your actual file location
    file_path = "words.txt"
    
    # Get words from file
    words = get_words_from_file(file_path)
    if not words:
        print("Error: No words available to generate sentences. Exiting.")
        return
    
    # Get user input for sentence length
    user_input = input("Enter the desired sentence length (2-20): ")
    
    # Validate input - exit immediately on any error
    try:
        length = int(user_input)
    except ValueError:
        print("Error: Please enter a valid integer. Exiting.")
        return
    
    if length < 2 or length > 20:
        print("Error: Sentence length must be between 2 and 20. Exiting.")
        return
    
    # Generate and print random sentence
    try:
        random_sentence = get_random_sentence(length, words)
        print(f"\nYour random sentence:")
        print(random_sentence)
    except Exception as e:
        print(f"Error generating sentence: {e}. Exiting.")

# Run the program
if __name__ == "__main__":
    main()