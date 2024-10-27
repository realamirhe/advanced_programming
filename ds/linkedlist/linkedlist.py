from __future__ import annotations

import gc
from typing import cast


class Node:
    def __init__(self: Node, value: int) -> None:
        self.value = value
        self.next = None
        self.prev = None  # doubly linked list


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def update(self, value: int, patch: int) -> None:
        found_node = self.find(value)
        if found_node is None:
            return

        found_node.value = patch

    def delete_first(self) -> None:
        # 0 element
        if self.head is None and self.tail is None:
            return

        self.head = cast(Node, self.head)  # force self.head to be type Node
        new_head = self.head.next
        self.head.next = None  # for better garbage collection
        self.head = new_head

    def delete_last(self) -> None:
        # 0 element
        if self.head is None and self.tail is None:
            return

        # 1 element
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return

        # +2 elements
        cur = self.head
        while cur.next.next is not None:  # type:ignore
            cur = cur.next  # type:ignore
        del cur.next  # type:ignore
        cur.next = None  # type:ignore
        self.tail = cur
        gc.collect()

    def add_last(self, value: int) -> None:
        new_node = Node(value)
        # is linked_list empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node  # type:ignore
        self.tail = new_node

    def add_fist(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head  # type:ignore
        self.head = new_node

    def find(self, value: int) -> Node | None:
        # 0 element
        if self.head is None and self.tail is None:
            return None

        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None