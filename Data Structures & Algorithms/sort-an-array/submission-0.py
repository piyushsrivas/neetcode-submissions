class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        l = self.sortArray(nums[:mid])
        r = self.sortArray(nums[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        sorted_array = []
        i = j = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                sorted_array.append(l[i])
                i += 1
            else:
                sorted_array.append(r[j])
                j += 1

        sorted_array.extend(l[i:])
        sorted_array.extend(r[j:])
    
        return sorted_array