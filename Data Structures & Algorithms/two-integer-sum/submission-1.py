class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffarr = [0] * len(nums)

        i = 0

        while i < len(nums):

            diffarr[i] = target - nums[i]

            i += 1

        i = 0

        while i < len(nums):

            subarr = nums[0:i] + nums[i+1:]

            if diffarr[i] in subarr:

                return sorted([i,subarr.index(diffarr[i]) + 1])

            i += 1

        return [0,0]
        