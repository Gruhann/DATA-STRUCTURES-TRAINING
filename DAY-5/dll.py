class node:
    def __init__(self,x):
        self.prev=None
        self.data = x
        self.next=None

class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_end(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t
    def add_beg(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
           t=node(x)
           t.next=self.head
           self.head.prev=t
           self.head=t
    def display(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next
        print()
    def reverse_display(self):
        t=self.tail
        while t!=None:
            print(t.data,end="<-")
            t=t.prev
        print()
    def search(self,x):
        if self.head==None:
            return None,None
        else:
            c=0
            b=0
            t=self.head
            q=self.tail
            while t!=q and t!=q.next:
                c+=1
                b-=1
                if t.data==x :
                    return "yes",c
                if  q.data==x:
                    return "yes",b
                t=t.next
                q=q.prev
            if t.data==x:
                return "yes",c
    def length_even_or_odd(self):
        h=self.head
        t=self.tail
        while t!=h and h!=t.next:
            h=h.next
            t=t.prev
        return "odd" if t==h else "even"
    def pal(self):
        h=self.head
        t=self.tail
        while t!=h :
            if h.data!=t.data:
                return "not palindrome"
            h=h.next
            t=t.prev
        return "palindrome"        
    def half(self):
        s=self.head
        f=self.head
        while f!=None and f.next!=None  :
            f=f.next.next
            s=s.next
        h=self.head
        # check for odd length (wrong output)
        t=s
        while t!=None:
            t.data,h.data=h.data,t.data
            t=t.next
            h=h.next

            
        a.display()  
    def change_link(self):
        curr=self.head
        curr_n=self.head.next
        t=self.head
        while curr_n:
            curr.next=curr_n.next
            curr_n.next=curr
            curr_n.prev=t
            curr.prev=curr_n
            curr,curr_n=curr_n,curr
            t=curr_n
            curr=curr.next.next
            curr_n=curr_n.next.next
            
        a.display()
    def paranthesis_check(self):
        b=list()
        t=self.head
        c=1
        flag=1
        while t.next:
            if t.data in ']})':
                flag=0
                break
            if t.data in '({[':
                b.append(t.data)
            elif t.data == ')' and '(' == b[-1]:
                b.pop()
            elif t.data == ']' and '[' == b[-1]:
                b.pop()
            elif t.data == '}' and '{' == b[-1]:
                b.pop()
            elif t.data !=b[-1]:
                break
            t=t.next
            c+=1
        return -1 if len(b)==0 and flag==1 else c
    def diff_evensum_oddsum(self,t,osum,esum):
        if t == None:
            return abs(esum-osum)
        if t.data % 2 == 0:
            return self.diff_evensum_oddsum(t.next,osum,esum + t.data)
        else:
            return self.diff_evensum_oddsum(t.next,osum + t.data,esum)
    def no_of_prime(self,t,c):
        if t == None:
            return c
        # else:
            # a=0
            # for i in range(2,int(t.data**0.5)+1):
            #     if(t.data%i==0):
            #         a+=1
            #         break                  //simple way to find prime
            # if a==0:
            #     print(t.data)
            #     return self.no_of_prime(t.next,c+1)
            # return self.no_of_prime(t.next,c)
        def isprime(s,n):
                if s>=n//2+1:
                    return 1
                if n%s==0:
                    return 0
                return isprime(s+1,n)
        if isprime(2,t.data):
            c+=1
        return self.no_of_prime(t.next,c)
                

                
            

            
            
                
            

a=dll()
a.add_beg(1)
a.add_beg(2)
a.add_end(3)
a.add_end(4)
a.add_end(5)
a.add_end(6)
# a.add_end(7)
# a.add_end(8)
a.display()
# a.reverse_display()
# print(a.search(10))
# print(a.length_even_or_odd())
# print(a.pal())
# a.half()
# a.change_link()
# print(a.paranthesis_check())
# print(a.diff_evensum_oddsum(a.head,0,0))
print("count of primes is ",a.no_of_prime(a.head,0))
