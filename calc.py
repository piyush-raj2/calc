def divide(x,y):
	if y == 0:
		print("Division by zero error..")
		return None
	else:
		return (x/y)

def multiply(x,y):
	return (x*y)


def add(x,y):
	return (x+y)

def subtract(x,y):
	return (x-y)

def main():
	a = 7, b = 8
	print("Add operation for a = ", a, " and b = ", b, " is ", add(a,b))

	print("Subtract operation for a = ", a, " and b = ", b, " is ", subtract(a,b))


	print("Multiply operation for a = ",a," and b = ",b, " is ", multiply(a,b))



if __name__ == '__main__':
	main()
	
