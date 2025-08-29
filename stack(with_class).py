class stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)

# creating object
mystack=stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)


print("Push Element : ",mystack.stack)
print(("Pop : ",mystack.pop()))
print("Stack after Pop : ",mystack.stack)
print("stack for peek : ",mystack.peek())
print("Is Empty : ",mystack.isEmpty())
print("Length is : ",mystack.size())
#
