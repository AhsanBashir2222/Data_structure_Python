queue=[]

queue.append("Ahsan")
queue.append("Salman")
queue.append("Usman")

print("Queue : ",queue)
#peek for return first element
peek=queue[0]
print("Peek : ",peek)
#pop:Remove and return first
pop=queue.pop(0)
print("Popped : ",pop)
#Returning queue
print("Queue : ",queue)
#for empty
isempty=not bool(queue)
print("is Empty : ",isempty)
print("Size of Queue :",len(queue))