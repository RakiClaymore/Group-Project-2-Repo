class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.child_count = 0
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
        lower_word = word.lower()
        # Reverse the word (this way finding the ends of words that match will be easier to determine words that rhyme)
        reversed_word = lower_word[::-1]
        # Iterate through each character in word
        for char in reversed_word:
            # Check if character is already in the Trie
            index = ord(char) - ord('a')
            # If not, create a new node
            if not curr.children[index]:
                curr.children[index] = TrieNode()
                curr.child_count += 1
            # Move curr to point to the new node
            curr = curr.children[index]
        # Flag the end of the word as true
        curr.isEndofWord = True
        # Save the original word in the node
        curr.word = originalWord

    def find_last_branch_node(self, word):
        # Point to the root
        curr = self.root
        last_branch = self.root
        # Make the word lowercase
        lower_word = word.lower()
        # Reverse the word
        reversed_word = lower_word[::-1]
        # Iterate through each char in the word
        for char in reversed_word:
            # Check if char is in the Trie
            index = ord(char) - ord('a')
            # If not, return None
            if not curr.children[index]:
                return None
            # If the current node has more than one child, update last_branch to point to the curr node
            if curr.child_count > 1:
                last_branch = curr
            # Move curr to point to the new node
            curr = curr.children[index]
        # If the current node has more than one child, update last_branch to point to the curr node
        if curr.child_count > 1:
            last_branch = curr
        # Return last_branch
        return last_branch