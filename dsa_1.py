stack=[]

#push
stack.append('A')
stack.append('B')
stack.append('C')
print("stacck", stack)

#peek
topelement = stack[-1]
print("peek",topelement)

#pop
popelement= stack.pop()
print("pop", popelement)

print("stack after pop",stack)

isEmpty = not bool(stack)
print("isEmpty", isEmpty)

print("size", len(stack))
