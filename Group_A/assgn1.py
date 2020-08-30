"""
                                    FDS Assignment 1
                                        Group A
Name: Shamik S Ghadge
Roll no.: SECOA159

Problem Statement:In second year computer engineering class, group A student’s play cricket, group B students play
badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET
built-in functions)

"""


def cricket_and_badminton_both(cricket, badminton):
    """Function which returns the list of students who play cricket and badminton both."""
    req_list_1 = []  # List of students who play cricket and badminton both
    
    for i in cricket:
        for j in badminton:
            if i == j:
                if i not in req_list_1:
                    req_list_1.append(i)
    return req_list_1


def cricket_or_badminton(cricket, badminton):
    """Function which returns the list of students who play either cricket or badminton but not both"""
    common = []  # List of students playing cricket and badminton both
    req_list_2 = []  # List of students playing cricket or badminton but not both

    for i in cricket:
        for j in badminton:
            if i == j:
                if i not in common:
                    common.append(i)
    
    for i in cricket:
        if i not in common:
            req_list_2.append(i)

    for j in badminton:
        if j not in common:
            req_list_2.append(j)

    return req_list_2


def football_only(cricket, badminton, football):
    """Function which returns the number of students who play neither cricket nor badminton."""
    cricket_and_badminton = []  # List of students who play cricket and badminton
    req_list_3 = []  # List of students who play neither cricket nor badminton i.e. only play football

    for i in cricket:
        for j in badminton:
            if i not in cricket_and_badminton:
                cricket_and_badminton.append(i)
            if j not in cricket_and_badminton:
                cricket_and_badminton.append(j)

    for k in football:
        for m in cricket_and_badminton:
            if k not in cricket_and_badminton:
                if k not in req_list_3:
                    req_list_3.append(k)

    return len(req_list_3)


def cricket_and_football_not_badminton(cricket, badminton, football):
    """Function which returns the number of students who play both cricket and football but not badminton."""
    cricket_and_football = []  # List of students who play cricket and football both
    req_list_4 = []  # List of students who play cricket and football both but not badminton

    for i in cricket:
        for k in football:
            if i == k:
                if i not in cricket_and_football:
                    cricket_and_football.append(i)

    for a in cricket_and_football:
        for n in badminton:
            if a not in badminton:
                if a not in req_list_4:
                    req_list_4.append(a)

    return len(req_list_4)

    
group_a = ['Rahul', 'Kapil', 'Sarang', 'Sachin', 'Nikhil']  # List of students playing cricket
group_b = ['Rahul', 'Sagar', 'Sarang', 'Abhi', 'Amol']  # List of students playing badminton
group_c = ['Rahul', 'Kapil', 'Sarang', 'Abhi', 'Varad']  # List of students playing football

print(cricket_and_badminton_both(group_a, group_b))
print(cricket_or_badminton(group_a, group_b))
print(football_only(group_a, group_b, group_c))
print(cricket_and_football_not_badminton(group_a, group_b, group_c))
