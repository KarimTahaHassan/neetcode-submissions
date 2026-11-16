class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        print(nums)

        for i in range(len(nums)):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            t = nums[i]

            if t > 0:
                return res

            t = t*-1
            l,r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == t:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                elif nums[l] + nums[r] > t:
                    r -= 1
                elif nums[l] + nums[r] < t:
                    l += 1


        return res
            