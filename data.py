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

print(word_flipper('retaw'))
