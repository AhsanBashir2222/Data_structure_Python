class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
def Traverse(head):
    current=head
    while current:
        print(current.value,end="->")
        current=current.next
    print("null")

def insert(head,new_node,position):
    if position==1:
        new_node.next=head
        return new_node
    current=head
    for _ in range(position-2):
        if current is None:
            break
        current=current.next
    new_node.next=current.next
    current.next=new_node
    return head


node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list : ")
Traverse(node1)
newNode=Node(1)
node=insert(node1,newNode,2)
print("After insertion : ")
Traverse(node)

