from collections import deque
q=deque()
q.append(67)
q.append(45)
q.appendleft(28)
print("Queue:",q)
print("Removed:",q.popleft())
print("Front element:",q[0])
print("Removed:",q.popleft())
if not q:
    print("Queue is empty")
else:
    print("Queue is not empty")
print("Final Queue:",q)