#Assignment 3.1

#Get hours and pay from user and calculate pay. If hours > 40, the residual hours get 1.5 times in pay. 

hours = float(input("Enter hours:"))
rate = float(input("Enter rate:"))

if hours <= 40:
    pay = hours * rate
else :
    overtimePay = hours - 40
    pay = (40*rate) + (overtimePay * rate * 1.5)

print(pay) 