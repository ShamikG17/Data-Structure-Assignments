"""
                                FDS Assignment 2
                                    Group A

Name: Shamik S Ghadge
Roll no.: SECOA159

Problem Statement: Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency

"""


def calc_average(marks):
    """ Function which returns the average of the total score of the students. """
    add = 0
    for mark in marks:
        add = add + mark
    total = len(marks)
    avg = add / total

    return avg


def calc_max_min_marks(marks):
    """ Function which returns the minimum(excluding 0) and maximum score of the class in the form of a list. """
    result = []
    marks.sort()
    min_max = []
    min_max[:] = (value for value in marks if value != 0)
    least_score = min_max[0]
    highest_score = min_max[-1]

    result.append(least_score)
    result.append(highest_score)

    return result


def calc_absent(marks):
    """ Function which returns the count of absent students. """
    absent_count = 0
    for mark in marks:
        if mark == 0:
            absent_count += 1

    return absent_count


def calc_highest_frequency(marks):
    """ Function which returns the score with the highest frequency in the list. """
    highest_frequency_mark = 0
    marks.sort()
    frequency = []
    cnt = 0
    while cnt < len(marks):
        frequency.append(marks.count(marks[cnt]))
        cnt += 1

    frequency_dict = dict(zip(marks, frequency))

    max_value = max(frequency_dict.values())

    for mark, value in frequency_dict.items():
        if value == max_value:
            highest_frequency_mark = mark

    return highest_frequency_mark


# The score of all students

marks_list = [95, 85, 99, 88, 87, 70, 99, 88, 85, 87, 90, 95, 96, 0, 91, 0, 92, 0, 0, 0, 99, 98, 99, 97, 99, 90, 99]

#  Calling all the functions.

average_marks = calc_average(marks_list)
min_marks = calc_max_min_marks(marks_list)[0]
max_marks = calc_max_min_marks(marks_list)[1]
absent = calc_absent(marks_list)
most_frequency_score = calc_highest_frequency(marks_list)

#  Printing all the values

print(average_marks)
print(min_marks)
print(max_marks)
print(absent)
print(most_frequency_score)

