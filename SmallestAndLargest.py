number_One = int(input("Enter first number: "))
number_Two = int(input("Enter second number: "))
number_three = int(input("Enter third number: "))

sum = number_One + number_Two + number_three
print(f"The sum of the three numbers is  {sum}")

average = number_One + number_Two + number_three / 3
print(f"The average of the three numbers is {average}")

product = number_One * number_Two * number_three 
print(f"The product of the three numbers is {product}")
    #LARGEST NUMBER
if number_One >=  number_Two and number_One >= number_three:
    largest = number_One
    print(f"The largest number is {number_One}")
    
elif number_Two >= number_three and number_Two >= number_One:
    largest = number_Two
    print(f"The largest number is {number_Two}")
    
else: 
    largest = number_three
    print(f"The largest number is {number_three}")
    
    #SMALLEST NUMBER
if number_One <= number_Two and number_One >= number_three:
    smallest = number_One
    print(f"{number_One} is the smallest number")
    
elif number_Two <= number_One and number_Two <= number_three:
    smallest = number_Two
    print(f"{number_Two} is the smallest number")

else: 
    smallest = number_three
    print(f"{number_three} is the smallest number")

