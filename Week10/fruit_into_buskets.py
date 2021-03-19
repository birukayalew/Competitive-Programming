class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        max_fruit_amount = 0
        start = 0
        fruit_container = {}
        
        for end, fruit in enumerate(tree):
            fruit_container[fruit] = fruit_container.get(fruit,0) + 1
        
            while len(fruit_container) > 2:
                fruit_container[tree[start]] -= 1
                if fruit_container[tree[start]] == 0:
                    del fruit_container[tree[start]]
                start += 1
                
            max_fruit_amount = max(max_fruit_amount,end - start + 1)
        return max_fruit_amount
                
                
            
