class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0

    def isempty(self):
        return self.size == 0
    def size(self):
        return self.length

    def printqueue(self):
        temp = self.front
        while temp:
            print(temp.data,end="->")
            temp = temp.next

        print()

    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front=self.rear=new_node
            self.length+=1

        self.rear.next=new_node
        self.rear=new_node
        self.length+=1

    def peek(self):
        if self.isempty():
            return "Queue is empty"
        return self.front.data
    def dequeue(self):
        if self.isempty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length-=1
        if self.front is None:
            self.rear=None
        return temp.data



my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue : ",end="")
my_queue.printqueue()
print("Peek : ",my_queue.peek())
print("Dequeue : ",my_queue.dequeue())
print("Queue : ",end="")
my_queue.printqueue()
print("Is empty : ",my_queue.isempty())
print("Size of Queue : ",my_queue.size())