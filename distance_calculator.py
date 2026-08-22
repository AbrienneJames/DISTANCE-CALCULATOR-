# you are calling library "math"
import math

#you are asking the user for variable inputs
x1= float(int(input("What is your x1:")))
x2= float(int (input("What is your x2:")))
y1= float(int (input("What is your y1:")))
y2= float(int (input("What is your y2:")))

#The distance formula that uses math functions and the given variables
distance=math.sqrt(math.pow(x2-x1, 2) + math.pow( y2-y1, 2))

#you are showing the user the results of the computation
print("The distance between 2 points is:" , distance)