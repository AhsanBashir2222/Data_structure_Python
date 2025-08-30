class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def Traverse(head):
    current=head
    while current:
        print(current.data,end=" ")
        current=current.next
    print("null")

def delete_specific(head,node_to_delete):
    if head==node_to_delete:
        return head.next
    current=head
    while current.next and current.next!=node_to_delete:
        current=current.next

    if current.next is None:
        return head
    current.next=current.next.next
    return head

node1=Node(5)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

print("Before deletion :")
Traverse(node1)
node=delete_specific(node1,node3)
print("After deletion :")
Traverse(node1)
