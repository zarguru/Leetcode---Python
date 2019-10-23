## Leetcode 1032 Hard
---
### Python
---

```
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
```

```Python
class TreeNode:
    
    def __init__(self):
        # self.letter = val     # Don't need val
        self.children = {}
        self.isWord = False

class TrieNode:
    
    def __init__(self):
        self.root = TreeNode()
        # self.children = {}
    
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TreeNode()
            node = node.children[w]
        node.isWord = True
    
    def exists(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            else:
                node = node.children[w]
                if node.isWord:
                    return True
        # return False              # Don't forget this line! Turns out it doesn't make difference whether this line exists
    
         
    


class StreamChecker:
    
    def __init__(self, words: List[str]):   
        self.q = ''
        self.trie = TrieNode()
        for word in words:
            self.trie.insert(word[::-1])           # reverse the order to check every possible match for self.q[x:]
            
        

    def query(self, letter: str) -> bool:
        self.q = letter + self.q                    # reverse order by using letter + self.q
        return self.trie.exists(self.q)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
```
