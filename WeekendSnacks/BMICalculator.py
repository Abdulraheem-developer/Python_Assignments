weight = int(input("Enter your weight (In Kg): "))
height = int(input("ENter your height (In meters): "))

BMI = weight / (height * height)

if BMI < 18.5:
    print("You are underweight!")
elif BMI >= 18.5 or 24.9:
    print("You are Normal")
elif BMI >= 25 or 29.9:
    print("Egbon, You are overweight, please you need to watching your weight")
elif BMI >= 30:
    print("Omoo, You are obese!")
