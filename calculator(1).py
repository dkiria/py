#!/usr/bin/python
import math


def prn ():
	print ("---------------------------menu calculator----------------------------" + "\n")
	
	print ("PRESS : " + "\n" + "1 for add / sub / multi / div" + "\n" + "2 for number conversion (binary or hecax)" + "\n"  +"3 for pow or sqrt" +  "\n" + "4 for sin or cos" + "\n" + "5 for log" +  "\n" + "6 for exit" + "\n")
	print ("----------------------------------------------------------------------" + "\n")
	

prn()

number =6
z= input("give your choise " + "\n")


while z < number:

 
 if z==1:
	print("------------Your choice is : add/sub/multi/div ------------" + "\n")

	x= input("give your first number " + "\n" + "\n")
	print ("your number is : " + str (x) + "\n")
	y= input("give your second number " + "\n" + "\n")
	print ("your number is : " + str (y) + "\n")

	def add(x, y):
	    print "ADDING %d + %d" % (x, y)
	    return x + y

	def subtract(x, y):
	    print "SUBTRACTING %d - %d" % (x, y)
	    return x - y

	def multiply(x, y):
	    print "MULTIPLYING %d * %d" % (x, y)
	    return x * y

	def divide(x, y):
	    print "DIVIDING %d / %d" % (x, y)
	    return x / y
	print ("--------calc menu--------" + "\n")

	sum1 = add(x, y)
	sub1 = subtract(x, y)
	multi1 = multiply(x, y)
	div1 = divide(x, y)

	print ("\n" + "PRESS " + " 1 for sum " + " 2 sub " + " 3 for multi " + "4 for div" + "\n")
	print ("--------calc menu--------" + "\n")
	a= input("give your choise " + "\n" + "\n")
	if a==1:
		print("Your choice is sum")
		print "Sum: %d" % (sum1)
	if a==2:
		print("Your choice is sub")
		print "Sub: %d " % (sub1)
	if a==3:
		print("Your choice is multi")
		print "Multi: %d" % (multi1)
	if a==4:
		print("Your choice is div")
		print "Div: %d" % (div1)
 	
 	prn()
 	z= input("give your choise " + "\n")
		

 if z==2:
	print("------------Your choice is number conversion------------")
	guess = int(input("1 for binary or 2 for hecax:"))
	if guess ==1:
		print("Your choice is binary")
		x= input("give your number " + "\n" + "\n")
		print ("your number is : " + str (x) + "\n" + "The number you gave in binary is: " + "\n")
		print bin(x) [2:]
	elif guess==2:
		print("Your choice is hexadecimal")
		x= input("give your number" + "\n" + "\n")
		print ("Your number is : " + str (x) + "\n" + "The number you gave in hexadecimal is: " + "\n")
		print ( hex (x) + "\n" )
	prn()
 	z= input("give your choise " + "\n")
	 	
	 

 if z==3:
	print("------------Your choice is pow or sqrt------------")
	guess = int(input("1 for pow or 2 for sqrt:"))
	if guess ==1:
		print("Your choice is pow")
		x= input("give your number " + "\n" + "\n")
		y= input("give your pow" + "\n" + "\n")
		print "the result is : ", math.pow(x, y)
	elif guess==2:
		print("Your choice is sqrt")
		x= input("give your number " + "\n" + "\n")
		print "the result is : ", math.sqrt(x)
	prn()
 	z= input("give your choise " + "\n")
	

 if z==4:
	print("------------Your choice is sin or cos------------")
	guess = int(input("1 for sin or 2 for cos:"))

	if guess ==1:
		print("Your choice is sin")
		t= input("give radians" + "\n" + "\n")
		print "sin of " + str(t) + " radians is : ", math.sin(z)
		
	elif guess==2:
		print("Your choice is cos")
		t= input("give radians" + "\n" + "\n")
		print "cos of " + str(t) + " radians is : ", math.cos(z)
	prn()
 	z= input("give your choise " + "\n")
	
		
 if z==5:
	print("------------Your choice is log------------")
	guess = int(input("1 for sin or 2 for cos:"))
	if guess ==1:
		print("Your choice is log10")
	k= input("give a number" + "\n" + "\n")
	print "log10  of  " + str(k) + "  is : ", math.log10(k) 
	prn()
 	z= input("give your choise " + "\n")
