class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        answer = ""
        store = ""
        for word in dictionary:
            self.insert(word)
        successors = sentence.split(" ")
        for word in successors:
            res = self.search(word,self.trie,0,store)
            if res is None:
                answer += word + " "
            else:
                answer += res + " "
        return answer.rstrip()
            
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
    def search(self,word,trie,index,store):
        if trie.end == True or index == len(word):
            return store
        
        if word[index] in trie.children:
            store += word[index]
            return self.search(word,trie.children[word[index]],index + 1,store)
        
        return None
 
        
class Node:
    def __init__(self):
        self.children = {}
        self.end = False



