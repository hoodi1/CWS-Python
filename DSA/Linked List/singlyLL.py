class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def traversal(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            node = self.head
            while True:
                print(node.value,end=" ")
                node = node.next
                if node == None:
                    break

    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
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

    def searchSLL(self,nodeValue):
        if self.head == None:
            print("Singly Linked List is empty ")
        else:
            node = self.head
            while True:
                if node==None:
                    break
                if node.value == nodeValue:
                    print("Found")
                    return
                node = node.next
            print("Not Found")

    def deleteNode(self, location):
        if self.head == None:
            print("Cannot delete, Linked list is empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
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
                            node.next = None
                            self.tail = node
                            break
                        node = node.next
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
                tempNode.next = nextNode.next
            
    def deleteLL(self):
        self.head=None
        self.tail=None

singlyLinkedList=SLinkedList()
#singlyLinkedList.insertSLL(100,0)
#singlyLinkedList.insertSLL(200,0)
singlyLinkedList.insertSLL(50,-1)
singlyLinkedList.insertSLL(45,-1)
singlyLinkedList.insertSLL(15,-1)
singlyLinkedList.insertSLL(40,-1)
singlyLinkedList.insertSLL(4000,-1)
singlyLinkedList.insertSLL(1000,2)
#singlyLinkedList.insertSLL(121,200)
singlyLinkedList.traversal()
print()
#singlyLinkedList.searchSLL(15)
#singlyLinkedList.searchSLL(18)
singlyLinkedList.deleteNode(-1)
singlyLinkedList.deleteNode(2)
singlyLinkedList.traversal()
singlyLinkedList.deleteLL()
print()
singlyLinkedList.traversal()



""" for 2 nodes 
singlyLinkedList=SLinkedList()
node1=Node(54)
node2=Node(12)

singlyLinkedList.head=node1
singlyLinkedList.tail=node2
singlyLinkedList.head.next=node2
singlyLinkedList.traversal()

# print(singlyLinkedList.tail.value)
#print(singlyLinkedList.head.next.value)
#print(singlyLinkedList.tail)
"""