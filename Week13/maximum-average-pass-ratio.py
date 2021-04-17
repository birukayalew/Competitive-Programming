import heapq as heap
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #add a student in a class which has more change in pass ratio 
        pass_ratio = []
        pass_ratio_sum = 0
        for passed,total in classes:
            old_class = passed / total
            new_class = (passed + 1) / (total + 1)
            change = new_class - old_class
            heap.heappush(pass_ratio,(-1*change,passed,total))   #using max heap
        for i in range(extraStudents):
            change,passed,total = heap.heappop(pass_ratio)
            new_passed = passed + 1
            new_total = total + 1
            new_change = ((passed + 2) / (total + 2)) - (new_passed / new_total)
            heap.heappush(pass_ratio,(-1*new_change,new_passed,new_total))
        for change,passed,total in pass_ratio:
            pass_ratio_sum += (passed / total)
        return pass_ratio_sum / len(classes)
