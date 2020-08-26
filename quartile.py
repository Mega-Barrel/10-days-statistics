'''
Task
	Given an array, X, of n integers, calculate the respective first quartile (Q1), second quartile (Q2),
	and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

Input Format

	The first line contains an integer, n, denoting the number of elements in the array.
	The second line contains n space-separated integers describing the array's elements.

Output
	The first line should be the value of Q1.
	The second line should be the value of Q2.
	The third line should be the value of Q3.
'''
from statistics import median

N = int(input().strip())
Element = list(map(int, input().strip().split(' ')))

def quartile(e):

    e.sort()
    
    len_number = len(e)

    if len_number % 2 != 0:

        first_half = e[:len(e)//2]
        second_half = e[len(e)//2 + 1:]

        quartile_1 = int(median(first_half))
        quartile_2 = int(median(e))
        quartile_3 = int(median(second_half))

    elif len_number % 2 == 0:

        first_half = e[:len(e)//2]
        second_half = e[len(e)//2:]

        quartile_1 = int(median(first_half))
        quartile_2 = int(median(e))
        quartile_3 = int(median(second_half))
    
    print(quartile_1, quartile_2, quartile_3, sep='\n')

quartile(Element)