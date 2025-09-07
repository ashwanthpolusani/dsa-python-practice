# Question: Implement a Trie data structure with basic operations
# Operations: insert, search, traverse, find longest subsequence

class Node:
    """A node in the Trie structure."""
    def __init__(self):
        self.data: dict[str, Node] = {}
        self.flag: bool = False  # True if node represents end of a word

class Trie:
    """Trie data structure supporting insert, search, and traversal."""
    def __init__(self):
        self.root = Node()  # always start with a root node

    def insert(self, word: str) -> None:
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.data:
                node.data[char] = Node()
            node = node.data[char]
        node.flag = True  # mark the end of the word

    def search(self, word: str) -> bool:
        """Search for a word in the Trie. Returns True if found."""
        node = self.root
        for char in word:
            if char not in node.data:
                return False
            node = node.data[char]
        return node.flag
    
    def traverse(self, node: Node = None, prefix: str = "", words: list = None) -> list:
        """
        Traverse the Trie and return all words stored.
        """
        if words is None:
            words = []
        if node is None:
            node = self.root
        if node.flag:
            words.append(prefix)
        for char, next_node in node.data.items():
            self.traverse(next_node, prefix + char, words)
        return words

    def longest_subsequence(self) -> str:
        """
        Find the longest word stored in the Trie.
        """
        def dfs(node, prefix):
            longest = prefix if node.flag else ""
            for char, next_node in node.data.items():
                candidate = dfs(next_node, prefix + char)
                if len(candidate) > len(longest):
                    longest = candidate
            return longest
        return dfs(self.root, "")

if __name__ == "__main__":
    # Test cases
    trie = Trie()
    words = ["hello", "world", "hi", "hey", "helloworld"]
    for word in words:
        trie.insert(word)
    print("Searching for words:")
    for word in words:
        print(f"'{word}' exists: {trie.search(word)}")
    print("All words in Trie:")
    print(trie.traverse())
    print("Longest word in Trie:")
    print(trie.longest_subsequence())