class AllOne:

    def __init__(self):
        self.m = collections.defaultdict(int)

    def inc(self, key: str) -> None:
        self.m[key]+=1

    def dec(self, key: str) -> None:
        self.m[key]-=1
        if self.m[key] == 0:
            del self.m[key]

    def getMaxKey(self) -> str:
        res =""
        cnt = 0
        for k,v in self.m.items():
            if v>cnt:
                res=k
                cnt=v
        return res

    def getMinKey(self) -> str:
        res =""
        cnt = 99999999990
        for k,v in self.m.items():
            if v<cnt:
                res=k
                cnt=v
        return res  
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()