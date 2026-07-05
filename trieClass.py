class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndofWord = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Point to the root
        curr = self.root
        # Save the original word
        originalWord = word
        # Make the word lowercase
        word = word.lower()
        # Reverse the word (this way finding the ends of words that match will be easier to determine words that rhyme)
        word = word[::-1]
        # Iterate through each character in word
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
        curr.word = originalWord