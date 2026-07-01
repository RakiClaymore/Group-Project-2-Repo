class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndofWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            # Check if character is already in the Trie
            index = ord(char) - ord('a')
            # If not, create a new node
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            # Move curr to point to the new node
            curr = curr.children[index]
        # Flag the end of the word as true
        curr.isEndofWord = True