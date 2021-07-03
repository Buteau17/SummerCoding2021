#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

greeting=input("Welcome to the tip calculator!")
print(greeting)
bill=float(input("What was the total bill?$"))
tip =int(input("What percentage tip would you like to give 10, 12,or 15? "))
print(tip)
number_of_people=int(input("How many people to split the bill?"))
print(number_of_people)
bill_with_tip= tip /100 * bill +bill
payment_of_each_person=((bill_with_tip/number_of_people))
total_payment_per_person=round(payment_of_each_person,2)
print(f"Each person should pay:${total_payment_per_person}")