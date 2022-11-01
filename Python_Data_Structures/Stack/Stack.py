class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,data):
        self.stack.append(data)
        print(data,'is added')

    def pop(self):
        if(len(self.stack)!=0):
            val=self.stack.pop()
            print(val,'is pop from stack')
            return
        else:
            print('Stack is empty')
            return

    def peek(self):
        return self.stack[len(self.stack)-1]


    def print_Stack(self):
        if(len(self.stack)>0):
            for i in range(len(self.stack)-1,-1,-1):
                print(self.stack[i],end=' ')
            print()
        else:
            print('Stack is empty')

myStack=Stack()

myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)
myStack.print_Stack()

myStack.pop()
myStack.pop()
myStack.print_Stack()

print('peek:',myStack.peek())

'''
===== RESTART: C:\Users\Amazonian\Desktop\ps\Python-Datastructure\Stack.py =====
10 is added
20 is added
30 is added
40 is added
40 30 20 10 
40 is pop from stack
30 is pop from stack
20 10 
peek: 20
'''
