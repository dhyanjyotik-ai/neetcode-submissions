class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        while index > 0:
            current = current.next
            index -= 1
        return current.val
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(val)
        self.size += 1      

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return -1
        dummy = Node(-1)
        dummy.next = self.head
        current = dummy
        while index > 0:
            current = current.next
            index -= 1
        newNode = Node(val)
        newNode.next = current.next
        current.next = newNode
        self.head = dummy.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1
        dummy = Node(-1)
        dummy.next = self.head
        current = dummy
        while index > 0:
            current = current.next
            index -= 1
        current.next = current.next.next
        self.head = dummy.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)