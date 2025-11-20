miles = -1;

total = 0;
count = 0;

miles = int(input("Enter the miles driven (-1 to end): "))

while miles != -1:    
    total += miles
    gallons = float(input("Enter the gallons used: "))
    print(f"The miles per gallon used for this tanks was {miles / gallons:.2f}" )
    count += 1;
    
    
print(f"The overall average miles/gallon used was {total / count:.2f}  ")
