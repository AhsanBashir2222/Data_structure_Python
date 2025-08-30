class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def Find_Lowest(head):
    min_value=head.data
    current_node=head.next
    while current_node:
        if current_node.data<min_value:
            min_value=current_node.data
            current_node=current_node.next
        return min_value

node1=Node(5)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
print("The Lowest Value is : ",Find_Lowest(node1))
