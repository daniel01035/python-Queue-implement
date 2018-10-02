class queue:
    def __init__(self):
        self.que = []
        self.front = -1
        self.rear = -1
        self.isEmpty

    def push(self, n):
        self.que.append(n)
        self.rear += 1

    def pop(self):
        if self.isEmpty():
            return print("Queue is Empty.")
        else:
            self.front += 1

    def peek(self):
        if self.isEmpty():
            return"Queue is Empty."
        else:
            return self.que[self.front + 1]

    def getSize(self):
        return self.rear - self.front

    def check(self):
        return self.que[self.front + 1:self.rear + 1]

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False
