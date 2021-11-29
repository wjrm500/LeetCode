"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from __future__ import annotations
from typing import List

class ListNode:
    def __init__(self, value=0) -> None:
        self.value = value
        self.next = None
    
    def set_next(self, next: ListNode) -> None:
        self.next = next

class LinkedList:
    def __init__(self, nums: List[int]) -> None:
        self.last_node = None
        for num in nums:
            self.add_node(num)
    
    def add_node(self, num: int) -> None:
        new_node = ListNode(num)
        if self.last_node is None:
            self.base_node = new_node
        else:
            self.last_node.set_next(new_node)
        self.last_node = new_node

class Solution:
    @staticmethod
    def add_two_numbers(list1: LinkedList, list2: LinkedList) -> LinkedList:
        results = []
        for l in [list1, list2]:
            current_item = l.base_node
            i, result = 1, 0
            while current_item is not None:
                result += current_item.value * i
                current_item = current_item.next
                i *= 10
            results.append(result)
        total = sum(results)
        return LinkedList(list(map(int, reversed(str(total)))))


list1 = LinkedList([2, 4, 3])
list2 = LinkedList([5, 6, 4])

l = Solution.add_two_numbers(list1, list2)