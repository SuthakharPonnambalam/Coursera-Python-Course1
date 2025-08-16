#Assignment 3.3

#Get numberic grade between 0.0 and 1.0 and use if else logic to display letter grade. 

numericGrade = float(input("Enter score:"))
if(numericGrade > 1.0) :print("Error")

elif (numericGrade < 0.0) : print("Error")

else:
    if (numericGrade >= 0.9) : print("A")
    elif (numericGrade >=0.8): print("B")
    elif (numericGrade >=0.7): print("C")
    elif (numericGrade >=0.6): print("D")
    elif (numericGrade < 0.6): print("F")
