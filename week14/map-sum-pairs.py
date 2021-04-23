class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()
        self.seen = {}
        
    def insert(self, key: str, val: int) -> None:
        seen = True if key in self.seen else False
        self.insert_helper(key,0,val,self.trie,seen)
        self.seen[key] = val

    def sum(self, prefix: str) -> int:
        res = self.starts_with(prefix)
        if res:
            return res.value
        return 0
    
    def insert_helper(self,word,index,val,trie,seen):
        if seen:
            trie.value = trie.value - self.seen[word]  + val
        else:
            trie.value += val 
            
        if index == len(word):
            trie.end = True
            return
        
        if word[index] not in trie.children:
            trie.children[word[index]] = Node()
            
        return self.insert_helper(word,index + 1,val,trie.children[word[index]],seen)
    
    def search_helper(self,word,index,trie):
        if index == len(word):
            return trie
        if word[index] in trie.children:
            return self.search_helper(word,index + 1,trie.children[word[index]])
    
    def starts_with(self,prefix):
        return self.search_helper(prefix,0,self.trie)
        
    
class Node():
    def __init__(self):
        self.children = {}
        self.end = False
        self.value = 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
