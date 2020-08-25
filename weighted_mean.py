'''
Objective
	In the previous challenge, we calculated a mean. 
	In this challenge, we practice calculating a weighted mean. 

Task
	Given an array, X, of N integers and an array, W, representing the respective weights of 's elements, 
	calculate and print the weighted mean of X's elements. 
	Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

Input Format

	The first line contains an integer, N, denoting the number of elements in arrays X and W.
	The second line contains N space-separated integers describing the respective elements of array X.
	The third line contains N space-separated integers describing the respective elements of array W.

Sample Input

	5
	10 40 30 50 20
	1 2 3 4 5

Sample Output

	32.0

Formula

	sum(mean*weigh)/sum(weight)

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Input number
x = int(input().strip())

# mean number
y = list(map(int, input().strip().split(' ')))

# weight
z = list(map(int, input().strip().split(' ')))


def weight(y, z):


    result = round(sum([i*j for i,j in zip(y,z)])/ sum(z),1)
    return result

print(weight(y,z))
