'''
creating stack using arrays
'''

stack=  []

def push_element():
    stack.append(int(input("enter:")))
def pop_element():
    stack.pop()

while True:
    print("operation 1:push 2:pop 3:quit")
    choice = int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        pass
    print(stack)

    