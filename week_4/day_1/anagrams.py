from anagram_checker import anagramchecker


def show_menu():
    print("1: input a word")
    print("2: exit")

def user_input():
    word=input("enter a word: ").strip()

    while True:
        if word=="exit":
            return None
        if not word.isalpha():
            print("only letters and no spaces or numbers")
            continue
        if " " in word:
            print("only 1 word")
            continue

        return word
    
checker=anagramchecker("mini.txt")
while True:
    show_menu()
    x=int(input("enter your choice 1 or 2\n"))
    if x==1:
        word=user_input()
        if checker.is_valid_word(word):
            anagram=checker.get_anagrams(word)
            if anagram:
                print(f"Anagrams for your word: {', '.join(anagram)}")
            else:
                print("no anagrams found")
        else:
            print(f"{word} is an invalid word")
    elif x==2:
        print("goodbye")
        break
    else:
        print("invalid reponse")







