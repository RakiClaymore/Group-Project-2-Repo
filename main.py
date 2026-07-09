from trieClass import Trie
import time
import json

# Function to display the menu
def menu():
    print("\n")
    print("-" * 70)
    print("Welcome to Prime Rhyme, where we can help you find ways to rhyme!")
    print("Please note that this program searches for rhymes based on shared suffixes, so rhymes may not be perfect.")
    print("-" * 70)
    print("1. Run Rhymes with Trie")
    print("2. Run Rhymes with Hash Map")
    print("3. Run Rhymes with Trie and Hash Map")
    print("4. Exit")
    print("-" * 70)
    print("\n")

# Function to display loading dots
def loading(text, dots = 4):
    print(text, end = "", flush = True)
    for i in range(dots):
        time.sleep(0.05)
        print(".", end = "", flush = True)
    print("\n")

def main():
    with open("dictionary.json", "r") as file:
        dictionary = json.load(file)

    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    
    # Set up variables
    trie_rhyme = Trie()
    trie_results = []

    # While loop to guide users through the menu
    while True:

        menu()
        user_choice = input("Please input a menu option to find rhyme words: ")

        if user_choice == "1":
            try:
                rhyme_word = input("Please input word to rhyme: ")
                # Ensure the input is an actual word
                if not rhyme_word.isalpha():
                    raise ValueError

                loading(f"Scanning database for words that rhyme with '{rhyme_word}'")
                start_trie = time.perf_counter()
                trie.insert(rhyme_word)
                trie_results = trie.get_rhymes(rhyme_word)
                print(f"Here are the words we found that rhyme with '{rhyme_word}': {str(trie_results)}")
                end_trie = time.perf_counter()
                print(f"This search took {end_trie-start_trie:.8f} seconds.")

            except ValueError:
                print("Error. Please input a valid word.")

        elif user_choice == "2":
            # Rhyme with Hash Map
            continue

        elif user_choice == "3":
            try:
                rhyme_word = input("Please input word to rhyme: ")
                # Ensure the input is an actual word
                if not rhyme_word.isalpha():
                    raise ValueError

                loading(f"Scanning database for words that rhyme with '{rhyme_word}'")
                print("-" * 70)
                print("Results from Trie: ")
                start_trie = time.perf_counter()
                trie.insert(rhyme_word)
                trie_results = trie.get_rhymes(rhyme_word)
                print(f"Here are the words we found that rhyme with '{rhyme_word}': {str(trie_results)}")
                end_trie = time.perf_counter()
                print(f"This search took {end_trie - start_trie:.8f} seconds.\n")

                print("-" * 70)
                print("Results from Hash Map: ")
                # Rhyme with Hash Map

            except ValueError:
                print("Error. Please input a valid word.")

        elif user_choice == "4":
            print("\nThank you for using Prime Rhyme! Please come again soon. :)")
            break

        else:
            print("\nYou have entered an invalid menu option. Please input a number between 1 and 4.")
            continue

if __name__ == "__main__":
    main()