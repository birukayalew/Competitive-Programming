class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()
         
        

    def addWord(self, word: str) -> None:
        
        self.character_adder(word,0,self.trie)
        
    def character_adder(self,word,index,trie):
        if index == len(word):
            trie.end = True
            return

        if word[index] not in trie.children:
            trie.children[word[index]] = Node()

        return self.character_adder(word,index + 1,trie.children[word[index]])
        
        
    def search_helper(self,word,trie,index):
        
        if index == len(word):
            return trie.end
        
        if word[index] == '.':
            for key in trie.children:
                res = self.search_helper(word,trie.children[key],index + 1)
                if res:
                    return True
            
        elif word[index] in trie.children:
            return self.search_helper(word,trie.children[word[index]],index + 1)
        
        return False
    
    def search(self,word:str) -> bool:
        
        return self.search_helper(word,self.trie,0)

        
class Node:
    def __init__(self):
        self.children = {}
        self.end = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
