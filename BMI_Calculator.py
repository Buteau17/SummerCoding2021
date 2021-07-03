#summerCoding
#BMICalculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI=weight/(height)**2
Value_of_BMI=round(BMI,2)
print(Value_of_BMI)
if Value_of_BMI <18.5:
  print (f"Your BMI is {Value_of_BMI}, you are underweight.")
elif  Value_of_BMI<25:
  print (f"Your BMI is {Value_of_BMI}, you have a normal weight.")
elif Value_of_BMI<30:
  print (f"Your BMI is {Value_of_BMI}, you are overweight.")
elif Value_of_BMI<35:
  print (f"Your BMI is {Value_of_BMI}, you are obese.")  
else:
  print (f"Your BMI is {Value_of_BMI}, you are clinically obese.")    