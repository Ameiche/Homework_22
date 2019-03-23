class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            lastNode = self.head
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = newNode
    def prepend(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
    def insertAfterNode(self, prevNode, data):
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
    def printList(self):
        curNode = self.head
        while curNode.next != None:
            print(curNode.data)
            curNode = curNode.next
        if curNode.next == None:
            print(curNode.data)
    def deleteNode(self, key):
        curNode = self.head
        if curNode != None and curNode.data == key:
            self.head = curNode.next
            curNode = None
            return
        else:
            prev = None
            while curNode != None and curNode.data != key:
                prev = curNode
                curNode = curNode.next
            if curNode == None:
                print("The data is not found in the list")
                return
            else:
                prev.next = curNode.next
                curNode = None

# Testing the Linked List
linkedLst = linkedList()
linkedLst.append(5)
linkedLst.append(10)
linkedLst.printList()
linkedLst.prepend(15)
linkedLst.printList()
linkedLst.insertAfterNode(linkedLst.head.next, 6)
linkedLst.insertAfterNode(linkedLst.head.next.next, 8)
linkedLst.printList()
linkedLst.deleteNode(6)
linkedLst.deleteNode(20)
linkedLst.printList()
