def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = ''.join( str1.split() )
    list1 = [char for char in str1]
    list1.sort()
    
    str2 = ''.join( str2.split() )
    list2 = [char for char in str2]
    list2.sort()
    
    
    return list1 == list2

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    flip_list = []

    for i in our_string.split():
        flip_word = [char for char in i]
        flip_word.reverse()
        i = ''.join(flip_word)
        flip_list.append(i)

    return ' '.join(flip_list)


def hamming_distance(str1, str2):
    
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    count = 0
    if (len(str1) != len(str2)): 
        return None
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    
    return count
    # TODO: Write your solution here



# --- Data Structures -----

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head is None:
        self.head = Node(value)
        return
        
    node = self.head
    self.head = Node(value)
    self.head.next = node
    
    return None
    # pass

def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here    
    if self.head is None:
        self.head = Node(value)
        return
    node = self.head
    while node.next:
        node = node.next
    
    node.next = Node(value)
    
    return None

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    if self.head.value == value:
        return self.head
    
    node = self.head
    while node.next:
        if node.next.value == value:
            return node.next
        else:
            node = node.next
            
    return None

def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    if self.head.value == value:
        self.head = self.head.next 
        return
     
    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            break
        else:
            node = node.next
    
    return None

def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    node = self.head
    self.head = self.head.next
    
    return node.value

def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
    # TODO: Write function to insert here    
    linked_list = self.to_list()
    
    if pos > len(linked_list):
        linked_list.append(value)
    else:
        linked_list.insert(pos, value)
    
    self.head = None
    for item in linked_list:
        self.append(item)
    
    return None

def size(self):
    """ Return the size or length of the linked list. """

    # TODO: Write function to get size here
    linked_list = self.to_list()
    return len(linked_list)


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    # TODO: Write your function to reverse linked lists here
    reversed_list = LinkedList()
    prev_node = None
    
    for item in linked_list:
        node = Node(item)
        node.next = prev_node
        prev_node = node
    
    reversed_list.head = node
        
    return reversed_list

def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    node = linked_list.head
    if node is None:
        return False
    
    while node.next:
        node = node.next
        if node.next == linked_list.head.next:
            return True
    
    # TODO: Write function to check if linked list is circular
    return False


LinkedList.prepend = prepend
LinkedList.append = append
LinkedList.search = search
LinkedList.remove = remove
LinkedList.pop = pop
LinkedList.size = size
LinkedList.insert = insert

linked_list = LinkedList()
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(1)
linked_list.append(3)
linked_list.append(4)
linked_list.append(3)
linked_list.remove(1)
linked_list.remove(3)
linked_list.remove(3)
linked_list.pop()
linked_list.insert(3, 6)
#linked_list.insert(0, 2)

#print('len: ', linked_list.size())
print(linked_list.to_list())