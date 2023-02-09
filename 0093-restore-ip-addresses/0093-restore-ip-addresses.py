class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def valid(ip):
            if ip and 0 <= int(ip) <= 255:
                if len(ip) > 1 and ip[0] == '0':
                    return False
                return True
            return False

        def helper(l, r, k):
            if k == 1:
                if valid(r):
                    l += r
                    ans.append(l)
                return
            
            for i in range(1, len(s) + 1):
                temp = r[:i]
                if valid(temp):
                    helper(l + temp + ".", r[i:], k - 1)
                else:
                    break


        helper("", s, 4)
        return ans



