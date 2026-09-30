class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        sliceAmount = k%len(nums)
        nums[:] = nums[len(nums) - sliceAmount:] + nums[:len(nums) - sliceAmount]





        