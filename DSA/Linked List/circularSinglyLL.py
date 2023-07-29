class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSinglyLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def createCSLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        print("Circular Singly LL has been created")

    def insertCSLL(self,value,location):
        newNode = Node(value)
        if self.head==None:
            print("Circular SLL is empty")
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==-1:
                newNode.next=self.head
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    if tempNode.next==None:
                        print("Cannot add Location out of index")
                        break
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def deleteCSLL(self,location):
        if self.head == None:
            print("Cannot delete, Linked list is empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
                    
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while True:
                        if node == None:
                            break
                        if node.next == self.tail:
                            node.next = self.head
                            self.tail = node
                            break
                        node = node.next
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    if tempNode.next==self.head:
                        print("Cannot add Location out of index")
                        break
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def traversal(self):
        if self.head is None:
            print("There are no nodes in CSLL")
        else:
            tempNode = self.head
            while True:
                print(tempNode.value,end=" ")
                tempNode = tempNode.next
                if tempNode == self.head:
                    break
    def searchSLL(self,nodeValue):
        if self.head == None:
            print("Singly Linked List is empty ")
        else:
            node = self.head
            while True:
                if node.next == self.head:
                    break
                if node.value == nodeValue:
                    print("Found")
                    return
                node = node.next
            print("Not Found")


circularSinglyLL = CircularSinglyLL()
circularSinglyLL.createCSLL(100)
circularSinglyLL.insertCSLL(200, 0)
circularSinglyLL.insertCSLL(20, 0)
circularSinglyLL.insertCSLL(111, -1)
circularSinglyLL.insertCSLL(600, -1)
circularSinglyLL.insertCSLL(87, 3)
circularSinglyLL.insertCSLL(89, 3)
circularSinglyLL.traversal()
print()
circularSinglyLL.deleteCSLL(-1)
circularSinglyLL.deleteCSLL(3)
circularSinglyLL.deleteCSLL(0)
circularSinglyLL.traversal()
print()
circularSinglyLL.searchSLL(200)