"""
class Stack:
    
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
        
    # TODO Add the push method
    def push(self, data):
        # TODO: Add a conditional to check for full capacity
        if (self.next_index == len(self.arr)):
            self._handle_stack_capacity_full()
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1
        
    # TODO: Add the _handle_stack_capacity_full method
    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(len(old_arr)*2)]
        for i in range(len(old_arr)):
            self.arr[i] = old_arr[i]

    def size(self):
        counter = 0
        for element in self.arr:
            if element:
                counter += 1
        return counter
    # return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.num_elements == 0:
            return None
        popped = self.arr[0]
        self.arr = self.arr[1:]
        self.next_index -= 1
        self.num_elements -= 1
        return popped
"""

# Implement stack using linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1

    # TODO: Add the pop method
    def pop(self):
        if self.is_empty():
            return None
        popped = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return popped

    # TODO: Add the size method
    def size(self):
        return self.num_elements
    # TODO: Add the is_empty method
    def is_empty(self):
        return self.num_elements == 0

foo = Stack()
foo.push("Test!")
foo.push("Yes!")
# print(foo.head.value)

# Implementing Stacks as Python list
class PyStack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
     
    # TODO: Intiate stack object
    stack = PyStack()
    # TODO: Interate through equation checking parentheses
    for i in equation:
        if i == '(' or i == ')':
            stack.push(i)
    # TODO: Return True if balanced and False if not
    return stack.size() % 2 == 0

print(equation_checker('((3^2 + 8)*(5/2))/(2+6))'))

