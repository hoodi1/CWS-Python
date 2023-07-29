class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def createCDLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode

    def traversal(self):
        if self.head == None:
            print("Cannot travese, CDLL is empty")
        else:
            tempNode = self.head
            while True:
                print(tempNode.value, end=" ")
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
            print()

    def searchNode(self, searchValue):
        if self.head == None:
            print("Cannot travese, CDLL is empty")
        else:
            tempNode = self.head
            while True:
                if tempNode.value == searchValue:
                    print("Found")
                    break
                if tempNode == self.tail:
                    print("Not found")
                    break
                tempNode = tempNode.next

    def emptyCDLL(self):
        self.head = None
        self.tail = None

    def insertNode(self, location, value):
        if self.head == None:
            print("Cannot add, dll is empty")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode


circularDLL = CircularDoublyLL()
circularDLL.createCDLL(100)
circularDLL.insertNode(0, 9)
circularDLL.insertNode(0, 55)
circularDLL.insertNode(-1, 81)
circularDLL.insertNode(-1, 33)
circularDLL.insertNode(2, -20)
circularDLL.insertNode(2, -30)
circularDLL.traversal()
circularDLL.searchNode(-100)
circularDLL.emptyCDLL()
circularDLL.traversal()
