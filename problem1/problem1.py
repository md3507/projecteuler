'''
Problem 1: 
Not much to this, just to get into using git and starting up on projecteuler



If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

def problem1():
	ans = 0
	for i in range(0,1000):
		if (mult_3(i) or mult_5(i)):
			ans = ans + i
	return ans

def mult_3(num):
	if num % 3 == 0:
		return True
	else:
		return False

def mult_5(num):
	if num % 5 == 0:
		return True
	else:
		return False



if __name__ == "__main__":
	print(problem1())