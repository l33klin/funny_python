#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 16/10/2018 6:44 PM
@Author  : Jian
@Contact : l33klin@foxmail.com
@Site    : 
@File    : find_palindrome_in_linked_list.py
"""


class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None


def new_list(sa=None):
    head = None
    for char in sa:
        node = Node(char)
        if head:
            head.next = node
        else:
            head = node

    return head


def is_palindrome_link(head):

    if not isinstance(head, Node):
        return False

    if head.next is None:
        return True

    p1 = head
    p2 = head
    temp_list = list()

    while p2 and p2.next:
        temp_list.append(p1.data)
        p1 = p1.next
        p2 = p2.next.next

    if p2:  # 如果P2不是None，则说明链表长度是奇数,直接跳过中间元素的判断
        p1 = p1.next

    while p1:
        if p1.data != temp_list.pop():
            return False
        p1 = p1.next

    return True


n_list = new_list("abeeba")
print(is_palindrome_link(n_list))


