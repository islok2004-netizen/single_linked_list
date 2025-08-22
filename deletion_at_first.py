class node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=node(10)
b=node(20)
c=node(30)

a.next=b
b.next=c
head=a
head=head.next
current=head
while current!=None:
    print(current.data,end=" ")
    current=current.next