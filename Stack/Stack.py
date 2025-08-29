stack=[]

#for push
stack.append("Ahsan")
stack.append("Ahmad")
stack.append("Salman")

print("stack :",stack)

#for peek
new=stack[-1]
print("Peek : ",new)
#pop
pop=stack.pop()
print("Pop :",pop)
#After pop print Element
print("After Pop :",stack)

# is empty
isempty= not bool(stack)
print("Is_Empty : ",isempty)
#length
print("Length : ",len(stack))

