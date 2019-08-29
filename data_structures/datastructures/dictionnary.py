from math import inf

from keyed_item import KeyedItem
from linked_list import LinkedList, LinkedListNode
from doubly_linked_list import DoublyLinkedList, DoublyLinkedListNode
from binary_search_tree import BinarySearchTree


class BaseDictionnary:
    def search(self, key) -> KeyedItem:
        """Given a search key, return a pointer to the element in
        dictionary self whose key value is k, if one exists.
        """
        raise NotImplementedError

    def insert(self, item: KeyedItem):
        raise NotImplementedError

    def delete(self, item: KeyedItem):
        raise NotImplementedError

    def max(self) -> KeyedItem:
        """retrieve item with the largest key"""
        raise NotImplementedError

    def min(self) -> KeyedItem:
        """retrieve item with the smallest key"""
        raise NotImplementedError

    def predecessor(self, item: KeyedItem) -> KeyedItem:
        """retrieve the item whose key is immediately before"""
        raise NotImplementedError

    def successor(self, item: KeyedItem) -> KeyedItem:
        """retrieve the item whose key is immediately after"""
        raise NotImplementedError
