import datetime
#datetime.datetime.now() --> returns date and time of my machine as a string
def q1():
	adds_15 = lambda a: a + 15
	multiply = lambda x,y: x * y

	input1 = int(input("enter a number: "))
	input2 = int(input("enter a number: "))
	input3 = int(input("enter a number: "))
	
	print(adds_15(input1))
	print(multiply(iput2, input3))
	
def q2():
	random_number = 3
	mul = lambda x:x*3
	print(mul(int(input("enter a number: "))))
	
def q3():
	my_list = [(3, 2), (2, 4), (1,5)]
	print(my_list[0])
	my_list.sort(key=lambda x:x[0])
	print(my_list)

def q4():
	current = datetime.datetime.now()
	print(current)
	extracted = lambda date_and_time : date_and_time.strftime(" Year: %Y \n Month: %m \n Day: %d")
	print(extracted(current))
	
def q5():
	start = [0, 1, 1]
	number = int(input("Which index of the fibonacci sequence do you want?"))
	if number >= 3:
		fib = lambda x : x[len(x) - 1] + x[len(x) - 2]
		for i in range(number - 3):
			start.append(fib(start))
	print(start)
	print("The result is: ", start[len(start) - 1])
	
done  = False	
print("1 - question 1 \t 4 - question 4")
print("2 - question 2 \t 5 - question 5")
print("3 - question 3")
print("Enter 0 to quit program")
while not done:
	question = int(input("Which question do you want to see? "))
	if question == 1:
		q1()
	elif question == 2:
		q2()
	elif question == 3:
		q3()
	elif question == 4:
		q4()
	elif question == 5:
		q5()
	elif question == 0:
		done = True
	else:
		print("not a valid question number")