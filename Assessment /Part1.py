import statistics
def compute_standard_deviation(numbers):
    """Compute the standard deviation of a list of numbers"""
    return statistics.stdev(numbers)

def find_second_largest(numbers):
    """Find the second largest number in a list"""
    return sorted(numbers)[-2]
def character_frequency_per_word(sentence):
    """Return a dictionary of character frequencies for each word in a sentence"""
    pass

def check_palindrome(numbers):
    """Check if a list of numbers is a palindrome"""
    if numbers [::-1]==numbers:
        return True
    else:
        return False

def longest_word_in_sentence(sentence):
    """Return the longest word in a sentence"""
    pass
def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into one sorted list"""
    return sorted(list1+list2)
def find_intersection(list1, list2):
    """Find the intersection (common elements) of two lists"""
    return list(set(list1).intersection(set(list2)))

def nth_fibonacci(n):
    """Calculate the nth Fibonacci number using both recursion and iteration"""
    pass
def reverse_words_in_sentence(sentence):
    """Reverse the words in a sentence while maintaining word order"""
    sentence=sentence.split(' ')
    new_sentence=sentence[::-1]
    final=""
    for word in new_sentence:
        final+=word+" "

    return final.strip()


def unique_characters_in_string(s):
    """Return all unique characters in a string"""
    