class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedlist:
    
    def __init__(self):
        self.head=None

    def insert_beginning(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

    def insert_ending(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
            newNode.prev=curr

    def insert_after(self,target,data):
        newNode=Node(data)
        if self.head is None:
            print('List is empty')
        else:
            curr=self.head
            while curr is not None:
                if curr.data==target:
                    if curr.next is not None:
                        newNode.next=curr.next
                    curr.next=newNode
                    newNode.prev=curr
                    break
                curr=curr.next
            else:
                print('Target value is not found to insert data')
                
    def insert_before(self,target,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr is not None:
                if curr.data==target:
                    newNode.next=curr
                    newNode.prev=curr.prev
                    if curr.prev is None:
                        self.head=newNode
                    else:
                        curr.prev.next=newNode
                    curr.prev=newNode
                    break
                curr=curr.next
            else:
                print('Target is not found')

    def inert_if_empty(self,data):
        if self.head is None:
            newNode=Node(data)
            self.head=newNode
        else:
            print('List is not empty')

    def delete_first(self):
        if self.head is None:
            print('List is empty')
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None

    def delete_last(self):
        if self.head is None:
            print('List is empty')
        elif self.head.next is None:
            self.head=None
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.prev.next=None
            curr.prev=None

    def delete_index(self,index):
        if self.head is None:
            print('List is empty')
        elif index>self.get_length() or index<0:
            print('Invalid index')
        elif index==0:
            self.delete_first()
        else:
            count=0
            curr=self.head
            while curr is not None:
                if count==index-1:
                    curr.next=curr.next.next
                    if curr.next is not None:
                        curr.next.prev=curr
                    break
                curr=curr.next
                count+=1

    def delete_target(self,target):
        if self.head is None:
            print('List is empty')
        elif self.head.next is None:
            if self.head.data==target:
                self.head=None
            else:
                print('Target value is not present')
        elif self.head.data==target:
            self.head=self.head.next
        else:
            curr=self.head
            while curr is not None:
                if curr.data == target:
                    break
                curr=curr.next
            else:
                print('Target is not present')
                return
            if curr.next is not None:
                curr.next.prev=curr.prev
                curr.prev.next=curr.next
            else:
                curr.prev.next=None
                curr.prev=None

    def get_length(self):
        count=0
        curr=self.head
        while curr is not None:
            curr=curr.next
            count+=1
        return count
        
    
    def print_list(self):
        if self.head is None:
            print('List is empty')
        else:
            print(None,end='<->')
            curr=self.head
            while curr is not None:
                print(curr.data,end='<->')
                curr=curr.next
            print(None)

    def print_reverse(self):
        if self.head is None:
            print('List is empty')
        else:
            print(None,end='<->')
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            while curr is not None:
                print(curr.data,end='<->')
                curr=curr.prev
            print(None)
    
    
dl=DoublyLinkedlist()
dl.insert_beginning(10)
dl.insert_beginning(20)
dl.insert_beginning(30)
dl.insert_beginning(40)
dl.insert_beginning(50)
dl.print_list()

dl.print_reverse()

dl.insert_ending(60)
dl.insert_ending(70)
dl.insert_ending(80)
dl.insert_ending(90)
dl.print_list()

dl.inert_if_empty(100)

dl.insert_after(900,55)
dl.insert_after(90,55)
dl.print_list()

dl.insert_before(100,15)
dl.print_list()

dl.insert_before(50,45)
dl.print_list()

dl.delete_first()
dl.print_list()

dl.delete_last()
dl.print_list()

dl.delete_index(8)
dl.print_list()

dl.delete_target(400)
dl.print_list()




