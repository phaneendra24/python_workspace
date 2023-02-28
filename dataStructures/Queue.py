# queue = []

# def enqueue():
#     element = input("enter the element to be inserted:")
#     queue.append(element)
#     print(element,"is added in q")

# def dequeue():
#     if not queue:
#         print("Queue is empty")
#     else:
#         e= queue.pop(0)
#         print("removed element",e)
# def display():
#     print(queue)

# while True:
#     print("select operation 1.add 2.Remove 3.show")
#     choice = int(input())

'''
Queue module
'''
# implementing stack using queue 

# from queue import LifoQueue

# s= LifoQueue(maxsize=3)
# print(s.qsize())

# s.put('a')
# s.put('b')
# s.put('c')
# print(s.full())
# print(s.empty())
# print(s.qsize())
# print(s.get())

# s.mutex()
'''
queue
'''
# import queue

# L = queue.Queue(maxsize=5)

# L.put(10)
# L.put(20)

# print(L.get())
# print(L.get())

'''
implementation of queue using LinkedList
'''

class Node : 
    def __init__(self,data) -> None:
        self.data= data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.last = None
    
    def enequeue(self,data):
        if self.last is None:
            self.head = Node(data)
            self.head = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return


a_queue = Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    #by using split, do will become a list, split 
    #work with string
    do = input('what would you like to do?').split()

    operation = do[0].strip().lower()
    if operation == 'enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation == 'dequeue':
        dequeued = a_queue.dequeue()
        if dequeued is None:
            print('Queue is empty.')
        else:
            print('Dequeued element:',int(dequeued))
    elif operation == 'quit':
        break

