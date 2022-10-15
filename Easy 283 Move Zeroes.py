'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #0 is pivot point, swap all non-zero element to front
        
        j = 0
        for i in range (len(nums)):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1 #j 必须得是非0的时候才能增加，所以当遇到0的时候，i继续往下走，j留在原地，然后i和j可以互换
            