class node:
    def __init__(self):
        self.d={}
        self.flag=0
l=[] 
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
        else:return False

    def prefix(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    
    def print_words_with_prefix(self,str):
        def fun(t,s):
            if t.flag==1:
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        s=''
        t=self.root
        for i in str:
            if(i in t.d):
                s+=i
                t=t.d[i]
            else:
                return 
        fun(t,s)

    def longest_word_prefix(self,str):
        # nonlocal l=[]
        def fun(t,s):
            if t.flag==1:
                l.append(s)
            for i in t.d:
                fun(t.d[i],s+i)
        s=''
        t=self.root
        for i in str:
            if(i in t.d):
                s+=i
                t=t.d[i]
            else:
                return 
        fun(t,s)
        
t1=tries()

n=int(input())
for i in range(n):
    a,s=input().split(" ")
    if a=="1":
        t1.insert(s)
    if a=="2":
        print(t1.search(s))
    if a=="3":
        print(t1.prefix(s))
    if a=="4":
        (t1.print_words_with_prefix(s))
        # print(l)
    t1.longest_word_prefix(s)
    
