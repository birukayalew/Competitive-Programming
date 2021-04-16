class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d1 = defaultdict(set)
        d2 = defaultdict(lambda : 0)
        answer = [0 for x in range(k)]
        for log in logs:
            d1[log[0]].add(log[1])
        for key in d1:
            curr = len(d1[key])
            d2[curr] += 1
        for key in d2:
            answer[key - 1] = d2[key]
        return answer
