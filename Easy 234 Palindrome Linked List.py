'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # 先把linkedList 储存进一个array， 好更方便比较左右pointer的数值是否一样
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        left, right = 0, len(nums) - 1

        while left <= right:

            if nums[left] != nums[right]:
                return False

            left += 1
            right -= 1

        return True
