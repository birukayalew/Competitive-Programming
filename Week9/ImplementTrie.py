class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        def character_adder(index,trie):
            if index == len(word):
                trie.end = True
                return
            
            if word[index] not in trie.children:
                trie.children[word[index]] = Node()
                
            return character_adder(index + 1,trie.children[word[index]])
        
        character_adder(0,self.trie)
    def search_helper(self,word,trie,index):
        if index == len(word):
            return trie
        
        if word[index] in trie.children:
            return self.search_helper(word,trie.children[word[index]],index + 1)
        
        return None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        result = self.search_helper(word,self.trie,0)
        
        return result and result.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        result = self.search_helper(prefix,self.trie,0)
        
        return result != None
        
        
class Node:
    def __init__(self):
        self.children = {}
        self.end = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
