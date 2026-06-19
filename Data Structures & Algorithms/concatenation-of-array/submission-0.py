class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans1 = []
        ans1 = nums
        for num in range(0, len(nums)):
            ans1.append(nums[num])
            ans = ans1
        return ans