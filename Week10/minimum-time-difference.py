class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        temp = []
        minimum = float('inf')
        for time in timePoints:
            curr1,curr2 = time.split(':')
            
            if curr1 == '00':
                curr1 = '24'
            temp.append([int(curr1) * 60,int(curr2)])
        temp.sort()
        for i in range(len(temp) - 1):
            minimum = min(minimum,abs((temp[i][0] - temp[i+1][0]) + (temp[i][1] - temp[i+1][1])))
            minimum = min(minimum,24*60 -minimum)
        
        minimum = min(minimum,abs(((24*60 - temp[-1][0]) + temp[0][0]) - (temp[-1][1] - temp[0][1])))
        return minimum
            
