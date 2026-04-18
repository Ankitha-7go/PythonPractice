from collections import deque
q=deque()
q.append(10)
q.append(20)
q.append(30)
print("Queue:",q)
print("Removed:",q.popleft())
print("Front element:",q[0])
if not q:
    print("Queue is empty")
else:
    print("Queue is not empty")
print("Final Queue:",q)