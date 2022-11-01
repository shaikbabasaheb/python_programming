class BinarySearchTree:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild is not None:
                self.lchild.insert(data)
            else:
                self.lchild=BinarySearchTree(data)
        else:
            if self.rchild is not None:
                self.rchild.insert(data)
            else:
                self.rchild=BinarySearchTree(data)

    def preOrder(self):
        print(self.key,end=' ')
        if self.lchild is not None:
            self.lchild.preOrder()
        if self.rchild is not None:
            self.rchild.preOrder()
    
    def inOrder(self):
        if self.lchild is not None:
            self.lchild.inOrder()
        print(self.key,end=' ')
        if self.rchild is not None:
            self.rchild.inOrder()

    def postOrder(self):
        if self.lchild is not None:
            self.lchild.postOrder()
        if self.rchild is not None:
            self.rchild.postOrder()
        print(self.key,end=' ')

    def search(self,data):
        if self.key == data:
            print('Node is found')
            return
        if self.key > data:
            if self.lchild is not None:
                self.lchild.search(data)
            else:
                print('Node is not found')
        else:
            if self.rchild is not None:
                self.rchild.search(data)
            else:
                print('Node is not found')

    def minNode(self,node):
        curr=node
        while curr.lchild is not None:
            curr=curr.lchild
        return curr

    def maxNode(self,node):
        curr=node
        while curr.rchild is not None:
            curr=curr.rchild
        return curr
    
    def delete(self,data,root):
        if self is None:
            return None

        if self.key > data:
            if self.lchild is not None:
                self.lchild=self.lchild.delete(data,root)
            else:
                print('Node is not found')
        elif self.key < data:
            if self.rchild is not None:
                self.rchild=self.rchild.delete(data,root)
            else:
                print('Node is not found')
        else:
            if self.lchild is None:
                if self == root:
                    temp=self.minNode(self.rchild)
                    self.key=temp.key
                    self.rchild=self.rchild.delete(temp.key,root)
                    
                temp=self.rchild
                self=None
                return temp
            
            elif self.rchild is None:
                if self == root:
                    temp=self.maxNode(self.lchild)
                    self.key=temp.key
                    self.lchild=self.lchild.delete(temp.key,root)
                    
                temp=self.lchild
                self=None
                return temp
            
            temp=self.minNode(self.rchild)
            self.key = temp.key
            self.rchild=self.rchild.delete(temp.key,root)
            
        return self        
                

root=BinarySearchTree(10)
l=[12,89,67,65,20,77,26,11,10]
for i in l:
    root.insert(i)
print('Search operation: ')
root.search(10)

print('PreOrder traversal: ')
root.preOrder()
print()
print('InOrder traversal: ')
root.inOrder()
print()
print('PostOrder traversal: ')
root.postOrder()

print()
print('delete operation')
root.delete(65,root)
root.inOrder()

'''
= RESTART: C:\Users\Amazonian\Desktop\ps\Python-Datastructure\BInarySearchTree.py
Search operation: 
Node is found
PreOrder traversal: 
10 12 11 89 67 65 20 26 77 
InOrder traversal: 
10 11 12 20 26 65 67 77 89 
PostOrder traversal: 
11 26 20 65 77 67 89 12 10 
delete operation
10 11 12 20 26 67 77 89
'''


            
            
