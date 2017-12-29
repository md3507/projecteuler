'''
Problem 20

'''

def digit_sum(n):
	ans = 0
	n_str = str(n)
	for index in range(0,len(n_str)):
		ans = ans + int(n_str[index])
	return ans

def fact(n):
	if (n != 1):
		return ( fact(n-1) * n)
	return 1
	

if __name__ == "__main__":
	x = fact(100)
	print(digit_sum(x))