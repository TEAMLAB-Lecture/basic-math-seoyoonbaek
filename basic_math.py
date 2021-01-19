#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    number_list.sort()
    greatest_number = number_list[-1]

    return print(greatest_number)


def get_smallest(number_list):
    number_list.sort()
    smallest_number = number_list[0]

    return smallest_number


def get_mean(number_list):
    mean = sum(number_list)/len(number_list)

    return mean


def get_median(number_list):
    number_list.sort()
    list_len = len(number_list)
    
    if list_len%2 == 0:
        median = sum(number_list[list_len//2-1:list_len//2+1])/2
    else:
        median = number_list[list_len//2]

    return median



