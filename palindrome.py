#!/usr/bin/env python

# A small script to return the first palindrome of a given string
# A few assumptions are made for the running of the script: 
# 1. The given string can contain any Latin character and symbol
# 2. The string is not too long - we're using quicksort to sort the characters
# 3. The string is a palindrome, although the script does some checking to determine whether this is true
#
#
import sys

# Creates the palindrome for string s
def get_palindrome(s):
    sorted_s = quicksort(s)
    i = 0
    # There is only one unique character (a char that occurs odd number of times in the string) and it must be placed in the middle of the resulting palindrome
    unique_char = None
    palindrome = ""
    while i < len(sorted_s)-1:
        if sorted_s[i] != sorted_s[i+1]:
            # first is the unique char
            if unique_char is not None:
                # Already found another unique char, so this string is not a palindrome
                print("Cannot create palindrome!")
                return None
            unique_char = sorted_s[i]
            i += 1
        else:
            palindrome += sorted_s[i]
            i += 2
    if len(s) % 2 == 0:
        # Only palindromes with odd length have unique chars
        if unique_char is not None:
            print("This word is not a palindrome!")
            return None
        else:
            return palindrome + palindrome[::-1]
    else:
        if unique_char is None:
            # The unique char is the last character
            unique_char = sorted_s[-1:]
        return palindrome + unique_char + palindrome[::-1]
            

# Performs a quick sort on the input string
def quicksort(s):
    s_list = list(s)
    quicksort_inner(s_list, 0, len(s) - 1)
    return "".join(s_list)

# Helper for recursive sorting
def quicksort_inner(s_list, start, end):
    if start < end:
        splitp = part(s_list, start, end)
        quicksort_inner(s_list,start, splitp-1)
        quicksort_inner(s_list, splitp+1,end)

# Partition the char list into two parts
def part(s_list, start, end):
    pivot = s_list[end]
    left = start
    right = end - 1
    done = False
    while not done:
        while left <= right and s_list[left] <= pivot:
            left += 1
        while s_list[right] >= pivot and left<= right:
            right -= 1
        if left > right:
            done = True
	else:
            tmp = s_list[left]
            s_list[left] = s_list[right]
            s_list[right] = tmp
    
    tmp = s_list[end]
    s_list[end] = s_list[left]
    s_list[left] = tmp

    return left 

# palindrome.py {string} - the script accepts only one string at a time
if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Please enter string")
        sys.exit(1)
    s = sys.argv[1]
    print("Finding first palindrome of string %s" %s)
    pali = get_palindrome(s)
    if pali is None:
        # Already caught that error
        sys.exit(1)
    else:
        print("First palindrome for string %s is %s" %(s, pali))
        sys.exit(0)


