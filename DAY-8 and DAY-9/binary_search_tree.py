class node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None

    def add_element(self,curr,x):
        if curr is None:
            return node(x)
        else:
            if x>=curr.data:
                curr.right=self.add_element(curr.right,x)
            else:
                curr.left=self.add_element(curr.left,x)
        return curr
    
    def display_in(self,root):
        if root:
            self.display_in(root.left)
            print(root.data,end=" ")
            self.display_in(root.right)
    def display_pre(self,root):
        if root:
            print(root.data,end=" ")
            self.display_pre(root.left)
            self.display_pre(root.right)
    def display_post(self,root):
        if root:
            self.display_post(root.left)
            self.display_post(root.right)
            print(root.data,end=" ")

    def search(self,curr,x):
        if curr is None:
            return False
        if curr.data==x:
            return True
        elif x<curr.data:
            return self.search(curr.left,x)
        else:
            return self.search(curr.right,x)
        
    def sum_nodes(self,curr):
        if curr is None :
            return 0
        return curr.data+self.sum_nodes(curr.left)+self.sum_nodes(curr.right)
    def sum_nodes_even(self,curr):
        if curr ==None:
            return 0
        if curr.data%2==0:
            return curr.data+self.sum_nodes_even(curr.left)+self.sum_nodes_even(curr.right)
        else:
            return self.sum_nodes_even(curr.left)+self.sum_nodes_even(curr.right)
    def absolute_diff(self,curr):
        if curr ==None:
            return 0
        if curr.data%2==0:
            return curr.data+self.absolute_diff(curr.left)+self.absolute_diff(curr.right)
        else:
            return -curr.data+self.absolute_diff(curr.left)+self.absolute_diff(curr.right)
    def height(self,curr):
        if curr == None:
            return -1
        else:
            return max(self.height(curr.left),self.height(curr.right))+1
    def balanced(self,curr):
        print(self.height(curr.left))
        print((self.height(curr.right)))
        return abs(self.height(curr.left)-self.height(curr.right))<=1
    
    def leaf_count(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.leaf_count(root.left)+self.leaf_count(root.right)
    
    def sum_leaf(self,curr):
        if not curr:
            return 0
        if not curr.left and not curr.right:
            return curr.data
        return self.sum_leaf(curr.left)+self.sum_leaf(curr.right)
    
    def depth(self,curr,c):
        if curr is None:
            return c-1
        else:
            return max(self.depth(curr.left,c+1),self.depth(curr.right,c+1))
    
    def depth_ele(self,curr,x,c):
        if curr is None:
            return -1
        if curr.data==x:
            return c
        if curr.data>x:
            return self.depth_ele(curr.left,x,c+1)
        else:
            return self.depth_ele(curr.right,x,c+1)


a=tree()
a.root=a.add_element(a.root,10)
a.root=a.add_element(a.root,20)
a.root=a.add_element(a.root,2)
a.root=a.add_element(a.root,7)
a.root=a.add_element(a.root,1)
a.root=a.add_element(a.root,3)
a.root=a.add_element(a.root,15)
print(a.search(a.root,15))
a.display_in(a.root)
# print()
# a.display_pre(a.root)
print()
# a.display_post(a.root)
# print(a.sum_nodes(a.root))
# print(a.sum_nodes_even(a.root))
# print(abs(a.absolute_diff(a.root)))
# print(a.height(a.root))
# print("balanced " if a.balanced(a.root) else "Not balanced") 
# print(a.leaf_count(a.root))
print(a.sum_leaf(a.root))
print(a.depth(a.root,0))
print(a.depth_ele(a.root,1,0))

'''
inorder=1 5 6 7 8 10 20 25
pre order=10 5 1 7 6 8 20 25
post order=1 6 8 7 5 25 20 10 
'''