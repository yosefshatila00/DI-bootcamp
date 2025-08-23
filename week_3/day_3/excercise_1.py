import random
import os

def get_words_from_file(file_name="words.txt"):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, file_name)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()
            if not words:
                raise ValueError("The words file is empty")
            return words
    except FileNotFoundError:
        print(f"Error: Could not find '{file_name}' in {script_dir}")
        print("Please make sure the file exists in the same folder as this script.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)

def get_random_sentence(length):
    words = get_words_from_file()
    selected_words = []
    
    for _ in range(length):
        selected_words.append(random.choice(words))
    
    sentence = " ".join(selected_words).lower()
    return sentence

def main():
    print("This program generates a random sentence from words in a text file.")
    print("You can choose how many words you want in the sentence (between 2 and 20).")
    
    while True:
        try:
            number_words = int(input("Enter number of words between 2 and 20: "))
            
            if 2 <= number_words <= 20:
                break
            else:
                print("Please choose a number between 2 and 20.")
        except ValueError:
            print("Please enter a valid number.")
    
    sentence = get_random_sentence(number_words)
    print(f"\nYour random sentence:\n{sentence}")

if __name__ == "__main__":
    main()