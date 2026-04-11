class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,element):
        self.queue.append(element)
        print("Inserted:",element)
    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is empty")
        else:
            print("Removed:",self.queue.pop(2))
    def peek(self):
        if len(self.queue)==0:
            print("Queue is empty")
        else:
            print("Front element:",self.queue[0])
    def is_empty(self):
        if len(self.queue)==0:
            print("Queue is empty")
        else:
            print("Queue is not empty")
    def display(self):
        print("Queue elements:",self.queue)
q = Queue()
q.enqueue(67)
q.enqueue(78)
q.enqueue(35)
q.display()
q.dequeue()
q.peek()
q.is_empty()
q.display()