number = int(input("Enter a five-digit number: "))

if number < 10000 or number > 99999:
    print("This is not a five-digit number.")
else:
    d1 = number // 10000
    d2 = (number // 1000) % 10
    d3 = (number // 100) % 10
    d4 = (number // 10) % 10
    d5 = number % 10

    if d1 == d5 and d2 == d4:
        print(f"{number} is a palindrome!")
    else:
        print(f"{number} is not a palindrome.")

