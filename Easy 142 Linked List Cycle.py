'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''


# Solution 1: 更多的空间使用，因为使用了set 占用了space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# store in a set
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lookup = set()
        while head and head.next:
            if head not in lookup:
                lookup.add(head)
            else:
                return head
            head = head.next
        return None



#Solution 2: slow and fast pointer   【memory less】
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next           # fast pointer和slow pointer如果相遇
            if slow == fast:                # 前面都是基本操作 判断是否存在一个linked list loop
                slow1 = head                # 如果存在的话，寻找在哪个节点产生loop，新加入一个pointer
                while slow:                 # 如果slow所在的位置和slow1相等的话 就是loop产生
                    if slow == slow1:       # 没有的话就一直找
                        return slow
                    else:
                        slow = slow.next
                        slow1 = slow1.next
        return None 
