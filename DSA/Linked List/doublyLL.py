class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class doublySinglyLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def creatDoublyLL(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode

    def travarsal(self):
        if self.head == None:
            print("Cannot traverse, DLL is empty")
        else:
            tempNode = self.head
            while True:
                if tempNode == None:
                    break
                print(tempNode.value,end=" ")
                tempNode = tempNode.next
            print() 

    def reverseTraversal(self):
        if self.head == None:
            print("Cannot traverse, DLL is empty")
        else:
            tempNode = self.tail
            while True:
                if tempNode == None:
                    break
                print(tempNode.value,end=" ")
                tempNode = tempNode.prev 
            print() 

    def insert(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    tempNode = tempNode.next
                    index+=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def deleteNode(self, location):
        if self.head == None:
            print("Cannot delete, Doubly Linked List is empty.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head.next.prev = None
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    if tempNode.next == None:
                        print("Cannot delete, because location out of index")
                        return
                    tempNode = tempNode.next
                    index += 1
                tempNode.next.next.prev = tempNode
                tempNode.next = tempNode.next.next


doblyLL = doublySinglyLL()
doblyLL.creatDoublyLL(100)
doblyLL.insert(10,0)
doblyLL.insert(101,-1)
doblyLL.insert(102,1)
doblyLL.insert(34,2)
doblyLL.travarsal()
print()
doblyLL.deleteNode(3)
doblyLL.deleteNode(0)
#doblyLL.deleteNode(2)
#doblyLL.delete(3)
doblyLL.travarsal()