class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_beginning(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
        else:
            newNode.next=self.head
            self.head=newNode
            self.tail.next=self.head

    def insert_ending(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head

    def get_length(self):
        count=0
        if self.head is self.tail:
            return 1
        curr=self.head
        while True:
            curr=curr.next
            count+=1
            if curr is self.head:
                break
        return count
        

    def insert_index(self,index,data):
        newNode=Node(data)
        if self.get_length()<index or index<0:
            print('Invalid index')
        elif index==1:
            self.insert_beginning(data)
        elif index==self.get_length()-1:
            self.insert_ending(data)
        else:
            count=0
            curr=self.head
            while True:
                if count==index-1:
                    newNode.next=curr.next
                    curr.next=newNode
                    break
                curr=curr.next
                count+=1

    def delete_first(self):
        if self.head is None:
            print('List is empty')
        elif self.head is self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head

    def delete_last(self):
        if self.head is None:
            print('List is empty')
        elif self.head is self.tail:
            self.head=None
            self.tail=None
        else:
            curr=self.head
            while True:
                curr=curr.next
                if curr.next is self.tail:
                    break
            self.tail=curr
            curr.next=self.head

    def delete_index(self,index):
        if self.head is None:
            print('List is empty')
        elif index<0 or index>self.get_length():
            print('Invalid index')
        elif index==0:
            self.delete_first()
        elif index==self.get_length()-1:
            self.delete_last()
        else:
            count=0
            curr=self.head
            while True:
                if count==index-1:
                    break
                curr=curr.next
                count+=1
            curr.next=curr.next.next

    def print_list(self):
        if self.head is None:
            print('List is empty')
        else:
            curr=self.head
            print('Connetion',end='->')
            while True:
                print(curr.data,end='->')
                curr=curr.next
                if curr is self.head:
                    break
            print('Connetion')

cl=CircularLinkedlist()
cl.insert_at_beginning(10)
cl.insert_at_beginning(20)
cl.insert_at_beginning(30)
cl.insert_at_beginning(40)
cl.insert_at_beginning(50)
cl.print_list()

cl.insert_ending(60)
cl.insert_ending(70)
cl.insert_ending(80)
cl.print_list()

cl.insert_index(2,344)
cl.print_list()

cl.delete_first()
cl.print_list()

cl.delete_last()
cl.print_list()

cl.delete_index(2)
cl.print_list()

'''
= RESTART: C:/Users/Amazonian/Desktop/ps/Python-Datastructure/Linkedlist/CircularLinkedlist.py
Connetion->50->40->30->20->10->Connetion
Connetion->50->40->30->20->10->60->70->80->Connetion
Connetion->50->40->344->30->20->10->60->70->80->Connetion
Connetion->40->344->30->20->10->60->70->80->Connetion
Connetion->40->344->30->20->10->60->70->Connetion
Connetion->40->344->20->10->60->70->Connetion
'''
