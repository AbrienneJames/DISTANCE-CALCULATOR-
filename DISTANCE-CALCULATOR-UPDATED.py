## you are calling library "math"
import math

#you are asking the user for variable inputs
x1_firstvariable= float(int(input("What is your x1:")))
y1_secondvariable= float(int (input("What is your x2:")))
x2_thirdvariable= float(int (input("What is your y1:")))
y2_fourthvariable= float(int (input("What is your y2:")))

#The distance formula that uses math functions and the given variables is given below:
distance=math.sqrt(math.pow(x2-x1, 2) + math.pow( y2-y1, 2))

#you are showing the user the results of the computation
print("The distance between 2 points is:" , distance)

#This program allowed us to locate the distance between 2 points with only the effort of inputting 4 variables which will be used by the computer to calculate. 