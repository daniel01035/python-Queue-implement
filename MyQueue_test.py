from DataStructure_implement.MyQueue import queue

q = queue()
q.pop()
q.push(1)
print(q.peek())
q.push(2)
print(q.check())
q.push(3)
q.pop()
q.push(4)
print(q.check())
print(q.getSize())