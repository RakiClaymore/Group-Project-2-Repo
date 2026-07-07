from trieClass import Trie
import time


def main():
    # Test
    # Create a new Trie
    trie_start = time.perf_counter()
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
    # Get words
    results = []
    results = trie.get_rhymes("cat")
    # Print
    print("Words that rhyme with 'cat' or share the same ending: " + str(results))
    trie_end = time.perf_counter()
    print(f"Execution time: {trie_end - trie_start:.8f} seconds")

if __name__ == "__main__":
    main()