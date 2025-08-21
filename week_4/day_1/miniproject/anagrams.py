from anagram_checker import anagramchecker

def show_menu():
    print("1: Input a word")
    print("2: Exit")

def get_user_input():
    while True:
        word = input("\nEnter a word (or type exit to go back): ").strip()
        
        if word.lower() == 'exit':
            return None
        
        if not word:
            print("Please enter a word!")
            continue
            
        if not word.isalpha():
            print("Only alphabetic characters allowed!")
            continue
            
        return word

checker = anagramchecker("sowpods.txt")

while True:
    show_menu()
    
    try:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == '1':
            word = get_user_input()
            
            if word is None:  
                continue
                
            if checker.is_valid_word(word):
                anagrams = checker.get_anagrams(word)
                
                print(f"\nYOUR WORD: \"{word.upper()}\"")
                print("This is a valid English word.")
                
                if anagrams:
                    print(f"Anagrams for your word: {', '.join(anagram.upper() for anagram in anagrams)}")
                else:
                    print("No anagrams found for this word.")
            else:
                print(f"\nYOUR WORD: \"{word.upper()}\"")
                print("This is NOT a valid English word.")
                
        elif choice == '2':
            print("bye")
            break
            
        else:
            print("Invalid choice! Please enter 1 or 2.")
            
    except ValueError:
        print("Please enter a valid number (1 or 2)!")
    except KeyboardInterrupt:
        print("\n👋 Program interrupted. Goodbye!")
        break
    except Exception as e:
        print(f"An error occurred: {e}")