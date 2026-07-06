from trieClass import Trie
import time


def main():
    # Test
    # Create a new Trie
    trie_start = time.time()
    trie = Trie()
    # Insert
    trie.insert("cat")
    trie.insert("bat")
    trie.insert("rat")
    trie.insert("mat")
    trie.insert("boat")
    trie.insert("station")
    trie.insert("nation")
    trie.insert("ration")
    # Find last branch node
    last_branch = trie.find_last_branch_node("cat")
    # Get words
    results = []
    trie.get_words(last_branch, results)
    # Print
    print("Words that rhyme with 'cat' or share the same ending: " + str(results))
    trie_end = time.time()
    print(f"Execution time: {trie_end - trie_start} seconds")

if __name__ == "__main__":
    main()