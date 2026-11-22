class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:

        def searchNode(curr, word):
            for i in range(len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if searchNode(child, word[i+1:]):
                            return True
                    return False
                else:
                    if word[i] in curr.children:
                        curr = curr.children[word[i]]
                    else:
                        return False
            return curr.endOfWord

        return searchNode(self.root, word)
