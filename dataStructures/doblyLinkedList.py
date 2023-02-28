class node:
    def __init__(self,data) -> None:
        self.data = data
        self.previous = None
        self.next = None
    
class DLL:
    def __init__(self) -> None:
        self.head = None
    
    def LogTheList(self):
        temp = self.head
        if not temp:
            print("Meow list is empty")
            return
        else:
            while temp:
                print(temp.data,end=" <-> ")
                temp = temp.next

    def insertStart(self,data):
        newNode = node(data)
        temp = self.head
        temp.previous = newNode
        newNode.next = temp
        self.head = newNode
    
    def insertEnd(self,data):
        newNode = node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp
                
    def insertionAt(self,data,pos):
        newNode = node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        newNode.previous = temp
        newNode.next = temp.next
        temp.next.previous = newNode
        temp.next = newNode
    
    def deletestart(self):
        temp = self.head
        self.head= temp.next
        temp.next = None
    
    def deleteEnd(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            previous = previous.next
        previous.next = None
    
    def deletePosition(self,pos):
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev= prev.next
        prev.next = temp.next
        temp.next = None
    

obj = DLL()
n1 = node(1)
n2 = node(2)
n3 = node(3)

obj.head = n1
n1.previous = obj.head
n1.next = n2
n2.previous = n1
n2.next= n3

obj.insertionAt(777,2)

obj.LogTheList()
obj.deletestart()
obj.LogTheList()