# '''
# Helps to write efficient programs
# - linear - array/ linked list/stack / queue /matrix
# - non-linear - bianry tree / graphs / heap ./hash table 
# - linear -storing data sequentially
# - non-linear - storing data without any sequence

# static - arrays
# dynamic - list ,stack , queue
# '''
# '''
# Linked list - eg: train
#     - As the name says list of items which are linked with one another is called as linked list
#     -types:
#         1- singly linked list
#         2- doubly linked list
#         3- circular linked list
# '''
# '''
# creating linked list 
#     1- create the node 
#     2- partition the node with two segements data and none
#     3- add value into the blank node
#     4- Mark the node as head 
#     5- Create the next node by following the above steps
#     6- Establish link between first node and the second node

# Displaying Linked list :
# 	traversal is required from first node till tail node inorder to display linked list     
# '''

# class node():
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# class singleLinkedList():
#     def __init__(self) -> None:
#         self.head = None
    
#     def insertBeginning(self,data):
#         new_node = node(data)
#         new_node.next = self.head
#         self.head= new_node
    
#     def insertAtEnd(self,data):
#         new_node = node(data)
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
    
#     def insertWithPosition(self,pos,data):
#         new_node = node(data)
#         temp = self.head
#         for i in range(pos-1):
#             temp = temp.next
#         new_node.next = temp.next
#         temp.next= new_node
    
#     # def Deletion(self,pos):
#     #     temp = self.head
#     #     for i in range(pos-1):
#     #         temp = temp.next        
    
#     def display(self):
#         if(self.head == None):
#             print("linked list is empty")
#         else:
#             temp = self.head
#             while temp:
#                 print(temp.data)
#                 temp = temp.next

# obj = singleLinkedList()

# # n= node("w")
# # n1= node("i")
# # n2= node("n")
# # n3= node("n")
# # n4= node("e")
# # n5= node("r")


# n= node(1)
# n1= node(2)
# n2= node(3)
# n3= node(4)
# n4= node(5)
# n5= node(6)

# obj.head= n
# obj.head.next = n1
# n1.next=n2
# n2.next=n3
# n3.next=n4
# n4.next=n5

# obj.insertBeginning(0)
# obj.insertAtEnd(10)
# obj.insertWithPosition(2,0.5)
# obj.display()



# class linkedList: 
#     def __init__(self) -> None:
#         self.head = None
#     def append(self,data):
#         # if self.last_node = None:
#             # self.head = node(data)
#             # `





# # n = int(input("enter :"))

# # for i in range(n):
# #     data = int(input("enter your data"))
# #     obj.append(data)
# # print('linked list :')
# # obj.display()
    