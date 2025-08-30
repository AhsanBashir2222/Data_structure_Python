class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,element):
        self.queue.append(element)

    def isEmpty(self):
        return len(self.queue)==0
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    def size(self):
        return len(self.queue)



my_queue=Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

print("Queue : ",my_queue.queue)
print("Peek : ",my_queue.peek())
print("Dequeue : ",my_queue.dequeue())
print("After Dequeue : ",my_queue.queue)
print("Is Empty : ",my_queue.isEmpty())
print("Size of Queue : ",my_queue.size())