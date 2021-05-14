class Stack:
    
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
        
    # TODO Add the push method
    def push(self, value):
        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

foo = Stack()
foo.push("Test!")
foo.push("Yes!")
print(foo.arr)