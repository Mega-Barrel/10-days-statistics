'''

Task

	Given an array, X, of N integers, calculate and print the standard deviation. 
	Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format). 
	An error margin of +-0.1 will be tolerated for the standard deviation.

Input Format

	The first line contains an integer, N, denoting the number of elements in the array.
	The second line contains N space-separated integers describing the respective elements of the array.

Sample Input

	5
	10 40 30 50 20

Sample Output

	14.1
'''

n = int(input().strip())
element = list(map(int, input().strip().split(' ')))


def standard_deviation(ele):

    mean = sum(ele) / n

    variance = sum([(i - mean)**2 for i in ele]) / n
    standard_Deviation = round(variance ** 0.5,1)

    print(standard_Deviation)

standard_deviation(element)

