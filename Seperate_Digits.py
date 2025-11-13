number = 42339
  
firstNumber = number // 10000
secondNumber = (number // 1000) % 10
thirdNumber = (number // 100) % 10
fourthNumber = (number // 10) % 10
lastDigit = number % 10
  
print(f"{firstNumber}  {secondNumber}    {thirdNumber}    {fourthNumber}   {lastDigit}")



