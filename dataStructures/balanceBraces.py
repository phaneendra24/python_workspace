s = input("enter the pattern: ")
st= []
balanced = True

for char in s:
    if (char=='{' or char =='[' or char == '('):
        st.append(char)
    elif(char=='}'):
        if (len(st) and st.pop()!='{'):
            balanced= False
            break
    elif(char==')'):
        if (len(st) and st.pop()!='('):
            balanced= False
            break
    elif(char==']'):
        print(len(st))
        if (len(st) and st.pop()!='['):
            if(len(st)== 0):
                print("sucks")
            balanced= False
            break
    else:
        balanced = False
        break
if(balanced == False or len(st)):
    print("not balanced")
else:
    print("balanced")