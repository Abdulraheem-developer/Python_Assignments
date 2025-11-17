firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
thirdNumber = int(input("Enter the third number: "))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    largest= firstNumber;
    print(f"{firstNumber} is the largest number");
    
if secondNumber > firstNumber and secondNumber > thirdNumber:
    largest = secondNumber;
    print(f"{secondNumber} is the largest number")
    
    
else:
        print(f"{thirdNumber} is the largest number")
