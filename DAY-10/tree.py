v=[]
from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            def recur(root, val):
                if val < root.val:
                    if root.left == None:
                        root.left = Node(val)
                        return
                    recur(root.left, val)
                elif val > root.val:
                    if root.right == None:
                        root.right = Node(val)
                        return
                    recur(root.right, val)
            recur(self.root, val)
    def traverse(self):
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            print(root.val, end=' ')
            inorder(root.right)
        def preorder(root):
            if root == None:
                return
            print(root.val, end=' ')
            preorder(root.left)
            preorder(root.right)
        def postorder(root):
            if root == None:
                return
            postorder(root.left)
            postorder(root.right)
            print(root.val, end=' ')
        print("inorder:", end=' ')
        inorder(self.root)
        print()
        print("preorder:", end=' ')
        preorder(self.root)
        print()
        print("postorder:", end=' ')
        postorder(self.root)
        print()
    def left_v(self,root,c):
        if root==None:
            return
        if c not in v:
            print("root.data",root.val)
            v.append(c)
        self.left_v(root.left,c+1)
        self.left_v(root.right,c+1)
    def rightt_v(self,root,c):
        if root is None:
            return
        if c not in v:
            print("root.data",root.val)
        self.rightt_v(root.right,c+1)
        self.rightt_v(root.left,c+1)
    def top_v(self,root):
        if root is None:
            return
        d={}
        q=[(root,0)]
        while q:
            root=q[0][0]
            if root.left!=None:
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append((root.right,q[0][1]+1))
            if q[0][1] not in d:
                d[q[0][1]]=root.val
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
    def bottom_v(self,root):
        if root is None:
            return
        d={}
        q=[(root,0)]
        while q:
            root=q[0][0]
            if root.left!=None:
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append((root.right,q[0][1]+1))
            d[q[0][1]]=root.val
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
            

            
            





        

bst = BST()
bst.add(10)
bst.add(5)
bst.add(15)
bst.add(2)
bst.add(7)
bst.add(11)
bst.add(20)
bst.add(4)
bst.add(12)
bst.add(3)
bst.add(13)
bst.add(14)
bst.traverse()
bst.left_v(bst.root,0)
v=[]
print("`````````````````````````")
bst.rightt_v(bst.root,0)
print("``````````````````````````")
bst.top_v(bst.root)
print()
bst.bottom_v(bst.root)
