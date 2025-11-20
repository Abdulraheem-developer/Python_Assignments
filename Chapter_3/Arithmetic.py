values = []

for number in range(3):
    numbers = int(input("Enter three numbers: "))
    values.append(numbers)
    
total = values[0] + values[1] + values[2] 
print(f"The total is {total}")

average = (values[0] + values[1] + values[2]) / 3
print(f"The average is {average}")

largest = values[0]

if values[1] > largest:
    largest = values[1]
   
    
elif values[2] > largest:
    largest = values[2]
    

print(f"Largest is {largest}")
     
smallest = values[0]

if values[1] < largest:
    smallest = values[1]
   
    
elif values[2] < largest:
    smallest = values[2]
    


    
print(f"Smallest is {smallest}")
          
