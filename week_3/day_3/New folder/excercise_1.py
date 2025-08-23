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


def get_random_sentence(words, length):
    random_strings=random.sample(words, length)
    sentence=" ".join(random_strings).lower().capitalize()
    return sentence

def main():
    print("the code asks you how many strings you want in a sentence and it takes randomly words from a txt file to make a sentence")
    number_words=int(input("enter number of words between 2 and 20\n"))
    
    if not 2<= number_words <=20:
        print("choose between the limit")
        return
    
    word=get_words_from_file()
    sentence=get_random_sentence(word, number_words)
    print(sentence)


if __name__ == "__main__":
    main()

