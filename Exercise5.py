#Assignment 4.6

#Use functions to compute pay, given hours and rate. If hours > 40 the residual gets paid 1.5 times. 
def computepay(h, r):
    if(h < 40):
        pay = h * r
    else:
        resHours = h - 40
        pay = (40 * r) + (resHours * r * 1.5)
    return pay

hours = float(input("Enter hours:"))
rate = float(input("Enter rate:"))

pay = computepay(hours, rate)
print("Pay",pay)


