class Queue:
    def __init__(self):
        self.items = ""

    def enqueue(self, item):
        self.items += item

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return self.items

        
#Do not modify anything below this line
def test01():
    q = Queue()
    for c in "abcd":
        q.enqueue(c)
    return str(q)

def test02():
    q = Queue()
    for c in "abcd":
        q.enqueue(c)
    q.dequeue()
    return q.dequeue()
def test03():
    q = Queue()
    for c in "abcd":
        q.enqueue(c)
    q.dequeue()
    q.dequeue()
    return q.is_empty()

def test04():
    q = Queue()
    for c in "hide":
        q.enqueue(c)
    q.dequeue()
    q.dequeue()
    q.enqueue("e")
    q.enqueue("p")
    return str(q)