'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

'''


#使用字典查找
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = {} #n就是key，出现了几次就对应着value 
        for n in nums:
            if n not in count_nums.keys():
                count_nums[n] = 1
            else:
                count_nums[n] += 1

        return max(count_nums, key=count_nums.get) #get最后的key通过比较它们的value数值
