
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def add_beginning(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def add_ending(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode

    def add_after(self,target,data):
        newNode=Node(data)
        curr=self.head
        while curr is not None:
            if curr.data is target:
                break
            curr=curr.next
        if curr is not None:
            newNode.next=curr.next
            curr.next=newNode
        else:
            print('target value is not available')

    def add_before(self,target,data):
        newNode=Node(data)
        if self.head is None:
            print('List is empty')
            return
        if self.head.data==target:
            newNode.next=self.head
            self.head=newNode
            return

        prev=self.head
        curr=self.head.next
        while curr.next is not None:
            if curr.data is target:
                newNode.next=curr
                prev.next=newNode
                break
            prev=prev.next        
            curr=curr.next

    def add_if_empty(self,data):
        if self.head is None:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
        else:
            print('List is not empty')

    def delete_first(self):
        if self.head is None:
            print('List is empty')
        else:
            self.head=self.head.next

    def delete_last(self):
        if(self.head is None):
            print('List is empty')
        elif(self.head.next is None):
            self.head=None
        else:
            curr=self.head
            while curr.next.next is not None:
                curr=curr.next
            curr.next=None

    def delete_value(self,target):
        if self.head is None:
            print('List is empty')
        elif self.head.data is target:
            self.head=self.head.next
        else:
            prev=self.head
            curr=self.head.next
            while curr.next is not None:
                if curr.data is target:
                    prev.next=curr.next
                    break
                prev=prev.next
                curr=curr.next

    def delete_index(self,index):
        if self.head is None:
            print('List is empty')
        elif index>self.get_length() or index<0:
            print('Invalid index')
        elif index==0:
            self.insert_beginning(data)
        else:
            curr=self.head
            count=0
            while curr!=None:
                if count==index-1:
                    curr.next=curr.next.next
                    break
                curr=curr.next
                count+=1
            
                

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
            curr=self.head
            while curr is not None:
                print(curr.data,end='->')
                curr=curr.next
            print('None')
            

ll=Linkedlist()
ll.add_beginning(10)
ll.add_beginning(20)
ll.add_beginning(30)
ll.add_beginning(40)
ll.print_list()

ll.add_ending(50)
ll.add_ending(60)
ll.add_ending(70)
ll.add_ending(80)
ll.print_list()

ll.add_after(80,5)
ll.print_list()

ll.add_before(50,45)
ll.print_list()

ll.add_if_empty(10)

ll.delete_first()
ll.print_list()

ll.delete_last()
ll.print_list()

ll.delete_value(45)
ll.print_list()

print(ll.get_length())

ll.delete_index(3)
ll.print_list()

'''
= RESTART: C:\Users\Amazonian\Desktop\ps\Python-Datastructure\Linkedlist\Linkedlist.py
40->30->20->10->None
40->30->20->10->50->60->70->80->None
40->30->20->10->50->60->70->80->5->None
40->30->20->10->45->50->60->70->80->5->None
List is not empty
30->20->10->45->50->60->70->80->5->None
30->20->10->45->50->60->70->80->None
30->20->10->50->60->70->80->None
7
30->20->10->60->70->80->None
'''
















