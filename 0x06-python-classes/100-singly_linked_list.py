#!/usr/bin/python3

class Node:

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise ValueError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(self.__next_node, Node) or type(self.__next_node) is not None:
            raise ValueError("next node must be a Node object")
    

class SinglyLinkedList:

    def __init__(self):
        self.__head = None
        pass

    def sorted_insert(self, value):

        new_node = Node(value)

        if self.__head == None:
            self.__head = new_node
        else:
            print("$$")
            node = self.__head
            while node.next_node:
                print("while")
                node = node.next_node
            node.__next_node = new_node

    def __str__(self):
        list_values = ""
        node = self.__head

        while node is not None:
            print("###")
            list_values += str(node.data) + "\n"
            node = self.__head.next_node
            print(self.__head.next_node)

        return f"{list_values}"
