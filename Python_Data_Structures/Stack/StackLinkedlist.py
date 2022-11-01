class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class StackLinkedlist:
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0

    def push(self,data):
        newNode=Node(data)
        if(self.top==None):
            self.top=newNode
            self.bottom=newNode
            print(data,'push in Stack')
        else:
            newNode.next=self.top
            self.top=newNode
            print(data,'push in Stack')
        self.length+=1

    def pop(self):
        if(self.top is None):
            print('Stack is empty')
        else:
            temp=self.top.data
            self.top=self.top.next
            self.length-=1
            print(temp,'pop in Stack')
            if(self.length==0):
                self.bottom=None

    def print_Stack(self):
        if(self.top is None):
            print('Stack is empty')
        else:
            curr=self.top
            while(curr is not None):
                print(curr.data,end='->')
                curr=curr.next
            print('None')

    def peek(self):
        if(self.top is None):
            return None
        return self.top.data

stacklinked=StackLinkedlist()

stacklinked.push(10)
stacklinked.push(20)
stacklinked.push(30)
stacklinked.push(40)
stacklinked.print_Stack()

stacklinked.pop()
stacklinked.pop()
stacklinked.print_Stack()

print('peek:',stacklinked.peek())


'''= RESTART: C:/Users/Amazonian/Desktop/ps/Python-Datastructure/StackLinkedlist.py
10 push in Stack
20 push in Stack
30 push in Stack
40 push in Stack
40->30->20->10->None
40 pop in Stack
30 pop in Stack
20->10->None
peek: 20
'''
        
