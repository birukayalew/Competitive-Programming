class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter_logs, digit_logs, ans = [], [], []
        def check_log(s):
            temp = s.split()
            if temp[1].isnumeric():
                digit_logs.append(s)
            else:
                letter_logs.append([temp[1:], temp[0]])
                
        for log in logs:
            check_log(log)
            
        letter_logs.sort()
        for i in range(len(letter_logs)):
            temp = [letter_logs[i][1]]
            for log in letter_logs[i][0]:
                temp.append(log)
            ans.append(" ".join(temp))
            
        return ans + digit_logs
            
        
