'''

Objective
	
	In this challenge, we practice calculating the mean, median, and mode. 
	Check out the Tutorial tab for learning materials and an instructional video!

Task 

	Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
	If your array contains more than one modal value, choose the numerically smallest one.

	Note: Other than the modal value (which will always be an integer), 
		  your answers should be in decimal form, rounded to a scale of  decimal place (i.e., 12.3, 7.0 format).

Input Format

	The first line contains an integer, N, denoting the number of elements in the array.
	The second line contains N space-separated integers describing the array's elements.

Output Format

	Print 3 lines of output in the following order:
	
	1. Print the mean on a new line, to a scale of 1 decimal place (i.e., 12.3, 7.0).
	2. Print the median on a new line, to a scale of 1 decimal place (i.e., 12.3, 7.0).
	3. Print the mode on a new line; if more than one such value exists, print the numerically smallest one.

Sample Input
	
	10
	64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output

	43900.6
	44627.5
	4978

Mean: sum(x)/total Number
Median: (x4 + x5) / 2
Mode: max(repeated number)
'''

n = int(input())
array = list(map(int, input().split(' ')))

def stats(array):

    array1 = sorted(array)

    mean = sum(array1)/n
    
    median =  (array1[n // 2] + array1[-(n // 2 + 1)]) /2

    mode = max(array1, key=array1.count)

    print(mean)
    print(median)
    print(mode)

stats(array)   