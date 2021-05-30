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

def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    
    positive_list = [i for i in in_list if i > 0]
    
    if len(positive_list) == 0:
        return None
    
    for i in range(len(positive_list)):
        if positive_list[0] > positive_list[i]:
            positive_list[0] = positive_list[i]
            
    return positive_list[0] or None

def nextDay(year, month, day):
    if month == 12:
        if day < daysInMonth(year, month):
            return year, month, day + 1
            
        else:
            return year + 1, 1, 1
    else:
        if day < daysInMonth(year, month):
            return year, month, day + 1
            
        else:
            return year, month + 1, 1


def compareDate(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    else:
        if month1 < month2:
            return True
        else:
            return day1 < day2
    

def isLeapYear(year):
        if year % 4 == 0:
            if year % 100 != 0:
                return True
            elif year % 100 == 0 and year % 400 == 0:
                return True
            else:
                return False

def daysInMonth(year, month):
    months = [1, 3, 5, 7, 8, 10, 12]
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    elif month in months:
        return 31 
    return 30

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0
    while compareDate(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1

    return days


def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
print(testDaysBetweenDates())

#---- Recursion ----- 

def reverse_string(input):
    last_char = len(input)-1
    if len(input) == 1:
        return input[0]
    return input[last_char] + reverse_string(input[:last_char])

# print(reverse_string('abc'))

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


correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:
"""
def check_sudoku(squares):
    el_dict = {}
    def num_gen(item):
        i = 0
        while i < range(len(item)):
            yield i
            i += 1
    
    for square in squares:
        i = next(num_gen())
        el = square[i]
"""        

            




    
    
#print(check_sudoku(incorrect))
#>>> False

#print(check_sudoku(correct))
#>>> True

#print(check_sudoku(incorrect2))
#>>> False

#print(check_sudoku(incorrect3))
#>>> False

#print(check_sudoku(incorrect4))
#>>> False

#print(check_sudoku(incorrect5))
#>>> False


