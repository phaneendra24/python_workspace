class node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class stack:
    def __init__(self) -> None:
        self.head = None
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def push(self,data):
        if self.head ==None:
         self.head = node(data)
        else:
            newnode = node(data)
            newnode.next = self.head
            
    def pop(self,data):
        if self.isempty():
            return None
        else:
            poppedNode = self.head
            self.head = self.head.next
            poppedNode.next = None
            return poppedNode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print("stack Underflow")
        else:
            while(t!=None):
                print(t.data,end="")
                t=t.next
                if(t != None):
                    print(" -> ",end= "")
        return
if __name__ == "__main__":
    s= stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.display()
    print(s.peek())
    s.display()