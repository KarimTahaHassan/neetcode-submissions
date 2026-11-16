class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        total = 1
        for i in range(len(nums)):
            prefix[i] = total
            total = total * nums[i]

        total = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = total
            total = total * nums[i]

        res = []
        for i in range(0, len(nums)):
            res.append(prefix[i] * postfix[i])

        return res