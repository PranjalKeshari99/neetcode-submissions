class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans_length = 2*n

        ans = [0] * ans_length

        for i in range(ans_length):
            if ans_length < n:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-n]

        return ans




        