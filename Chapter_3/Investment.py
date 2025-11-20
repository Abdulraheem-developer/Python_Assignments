investment_Amount = int(input("How much are you investing: "))
interest = 7

for years in range(1, 31):
    investment_Amount += (investment_Amount * (interest / 100))
    print(f"You invested {investment_Amount:.2f} in year {years}")
