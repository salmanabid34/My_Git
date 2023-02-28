class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def print(self):
        if self.head is None:
            print("Linked List IS Empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr=llstr+str(itr.data)+("\n")
            itr=itr.next           
        print(llstr)
    def insert_at_the_end(self):
        if(self.head is None):
            self.head=Node(self.data,None)
            return

    
if __name__ == '__main__':
    ll=linkedList()
    ll.insert_at_begining(8)
    ll.insert_at_begining(9)
    ll.print()