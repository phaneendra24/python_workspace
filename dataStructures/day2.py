# # Linked list exercise 

# class node:
#     def __init__(self,data) -> None:
#         self.data= data
#         self.next= None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
     
#     def LogTheList(self):
#         temp = self.head
#         if not temp:
#             print("Meow list is empty")
#             return
#         else:
#             while temp:
#                 print(temp.data,end="->")
#                 temp = temp.next
#     def insert(self,data):
#         new_node = node(data)
#         if self.head is None:
#             self.head = new_node
#             print("head inserted",new_node.data)
#         elif self.head.data >= new_node.data :
#             new_node.next= self.head
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next and new_node.data > current.next.data:
#                 current= current.next
#             new_node.next= current.next 
#             current.next = new_node
    
#     def deleteByelement(self,data):
#         temp = self.head
#         while temp:
#             if temp.next.data == data:
#                 temp.next = temp.next.next
#             temp = temp.next


    
            
# if __name__== '__main__':
#     obj = LinkedList()

#     obj.insert(0)
#     obj.insert(5)
#     obj.insert(2)
#     obj.insert(3)

#     obj.deleteByelement(2)
#     obj.LogTheList()


# creating our own modules in python
# import riddle 

# riddle.printing()

# print(__name__)



# print("before executions")

# def f1():
#     print("first function")

# def f2():
#     print("second function")

# def f3():
#     print("third function")

# if __name__ == '__main__':
#     f1()
#     f2()
#     f3()

# print("name:", __name__)

