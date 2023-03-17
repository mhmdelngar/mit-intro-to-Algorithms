from asyncio.windows_events import NULL
from curses.ascii import NUL
from re import I, S, X


class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next =self.head    
            self.head.prev=new_node
            self.head=new_node
        

    def insert_last(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node    

        

        

    def delete_first(self):
        x = None
        if self.head is None:
            return x
        if self.head.next is None:
            m=self.head
            self.head=None
            self.tail=None
        else:
            m=self.head
            self.head=m.next
        
        x=m
        return x

    def delete_last(self):
        x = None
        if self.head is None:
            return x
        x=self.tail
        if self.tail.prev is None:
            self.head=None
            self.tail=None
        else:
            self.tail=x.prev
            self.tail.next=None            
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head=x1
        L2.tail=x2
        if self.head==x1:
            self.head=x2.next
            
        elif self.tail ==x2:
            self.tail=x1.prev
             
        else:
            x1.prev.next=x2.next 
            x2.next.prev=x1.prev.next
    
        x1.prev=None
        x2.next=None
        return L2

    def splice(self, x, L2):
        xn = x.next
        x1=L2.head
        x2=L2.tail
        L2.head=None
        L2.tail=None
        x1.prev=x
        x.next=x1
        x2.next=xn
        if xn:
            xn.prev = x2
        else:
            self.tail = x2 
        
        


        
        
