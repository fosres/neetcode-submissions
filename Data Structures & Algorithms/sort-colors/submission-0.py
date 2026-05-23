class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        table = [0] * 3

        for i in range(len(nums)):

            if nums[i] == 0:

                table[0] += 1

            elif nums[i] == 1:

                table[1] += 1

            elif nums[i] == 2:

                table[2] += 1

        i = 0

        j = 0

        print(f"table: {table}")

        while i < len(table):

            c = 0

            while c < table[i]:

                nums[j] = i

                c += 1

                j += 1

            i += 1
        