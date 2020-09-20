"""
                        FDS Assignment 3
                            Group A

Name: Shamik S Ghadge
Roll no.: SECOA159

Problem Statement:
Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string

"""


def calc_longest_word(string):
    str_list = string.split()
    max_len = 0
    for word in str_list:
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word

    return longest_word


def char_frequency(char, string):
    freq_dict = {}
    for letter in string:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1
    result = freq_dict[char]

    return result


def check_palindrome(string):
    palindrome = 0
    if string == string[::-1]:
        palindrome = True
    else:
        palindrome = False

    return palindrome


def find_occurrence(substring, string):
    index = string.find(substring)

    return index


def word_count(string):
    count_dict = {}
    words = string.split()
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    return count_dict


str1 = (input("Enter the string: "))
substring1 = input("Enter substring: ")

print("Longest word: ", calc_longest_word(str1))
print("The frequency of characters is: ", char_frequency(substring1, str1))
print("Palindrome: ", check_palindrome(str1))
print("Index of substring: ", find_occurrence(substring1, str1))
print("Word count: ", word_count(str1))
