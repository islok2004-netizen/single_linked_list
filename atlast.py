
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

newnode=node(40)
current=head
while current.next !=None:
    current=current.next
current.next=newnode

# print last node also
temp=head
while temp is not None:
    print(temp.data, end=" ")
    temp=temp.next
