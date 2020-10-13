"""
                                    FDS Assignment 1
                                        Group B

Name: Shamik S Ghadge
Roll no.: SECOA159

Problem Statement: Write a Python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using 
                    a) Selection Sort 
                    b) Bubble sort and display top five scores.

"""

# Selection Sort
def selection_sort(marks):
    """Function to return a sorted list using the selection sort algorithm."""
    for i in range(len(marks)):
        min = i
        for j in range(i+1, len(marks)):
            if marks[min] > marks[j]:
                min = j

        marks[i], marks[min] = marks[min], marks[i]

    return marks


# Bubble Sort
def bubble_sort(marks):
    """Function to return a sorted list using the bubble sort algorithm."""
    for i in range(len(marks)):
        for j in range(len(marks)-i-1):
            if marks[j] > marks[j+1]:
                marks[j], marks[j+1] = marks[j+1], marks[j]

    return marks


# Driver code
percentage_list = []
n = int(input("Enter the number of students: "))
for i in range(n): 
    percentage = float(input("Enter the percentage: "))
    percentage_list.append(percentage)


selection_scores = selection_sort(percentage_list)[-5:]
bubble_scores = bubble_sort(percentage_list)[-5:]

print("Top 5 scores(using selection sort): ", selection_scores)
print("Top 5 scores(using bubble sort): ", bubble_scores)