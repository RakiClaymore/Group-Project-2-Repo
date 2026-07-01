class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndofWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
