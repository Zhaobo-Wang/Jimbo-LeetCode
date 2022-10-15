'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 创建一个dummynode list， compare list1 and list2 value， append in dummynode list
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:  #当list 1 和 list2 都有值时
            if list1.val < list2.val:
                tail.next = list1     #数值比较小的在tail
                list1 = list1.next    #更新一下新的list指针
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next    #更新一下新的tail
            
        if list1:   #如果只剩list1
            tail.next = list1   #剩下的全部都放在 List最后
        else:
            tail.next = list2
        return dummy.next  # 返回 dummy 后面的数值
                