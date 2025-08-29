class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class stack:
    def __init__(self):
        self.head=None
        self.size=0

    def isEmpty(self):
        return self.size==0
    def stack_size(self):
        return self.size

    def push(self,value):
        new_node=node(value)
        if self.head:
            new_node.next=self.head

        self.head=new_node
        self.size+=1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty :)"
        popped_node=self.head
        self.head=self.head.next
        self.size-=1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty :)"
        return self.head.value

    def traverse(self):
        current=self.head
        while current:
            print(current.value, end="->")
            current=current.next
        print()



my_stack=stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Linked_list : ", end="")
my_stack.traverse()
print("Peek :",my_stack.peek())
print("Pop : ",my_stack.pop())
print("Linklist after pop : ", end="")
my_stack.traverse()
print("Is_empty :",my_stack.isEmpty())
print("Stack size : ",my_stack.stack_size())
