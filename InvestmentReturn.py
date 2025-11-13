principal  = 1000;
annual_rate = 7 / 100
number_of_years1 = 10
number_of_years2 = 20
number_of_years3 = 30

Ten_Years =  principal * (1 + annual_rate) ** number_of_years1
print(f"I would have made {Ten_Years} in 10 years");

twenty_years = principal * (1 + annual_rate) ** number_of_years2
print(f"I would have made {twenty_years} in 20 years");

thirty_years = principal * (1 + annual_rate) ** number_of_years3
print(f"I would have made {thirty_years} in 30 years");
