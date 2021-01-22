class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        checker=0
        listnumber=1
        while checker<len(target):
            if listnumber!=target[checker]:
                ans.append("Push")
                ans.append("Pop")
                listnumber+=1
            else:
                ans.append("Push")
                checker+=1
                listnumber+=1
            
                
        return ans
            
