weight = int(input("Enter your weight "))
height = int(input("Enter your height "))
tmp = weight / (height**2)
if tmp < 0.00185:
 print ("Underweight")
if tmp >= 0.00185 and tmp < 0.0025:
 print ("Normal")
if tmp >= 0.0025 and tmp < 0.003:
 print ("Overweight")
if tmp > 0.003:
 print ("Obesity")