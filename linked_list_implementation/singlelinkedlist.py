class Node:
    def __init__(self, datavalue = None):
        self.datavalue = datavalue
        self.next = None

class SingleLinkedList:
    def __init__(self, headvalue = None):
        headnode = Node(headvalue)
        self.head = headnode
        self.tail = headnode

    def __iter__(self):
        currentnode = self.head
        while currentnode is not None:
            currentnodeout = currentnode
            currentnode = currentnode.next
            yield currentnodeout

    def append(self, newvalue = None):
        newnode = Node(newvalue)
        if self.head.datavalue is None:
            self.head.datavalue = newvalue
            return
        self.tail.next = newnode
        self.tail = newnode

    def prepend(self, newvalue = None):
        newhead = Node(newvalue)
        if self.head.datavalue is None:
            self.head.datavalue = newvalue
            return
        oldhead = self.head
        self.head = newhead
        newhead.next = oldhead
    
    def insert(self, pos, newvalue):
        newnode = Node(newvalue)
        currentNode = self.head
        current_item_number = 0
        if pos > 0:
            while current_item_number < pos:
                lastNode = currentNode
                currentNode = currentNode.next
                current_item_number += 1
           
            lastNode.next = newnode
            newnode.next = currentNode

            if currentNode ==  None:
                self.tail = newnode
        elif pos == 0:
            self.prepend(newvalue)