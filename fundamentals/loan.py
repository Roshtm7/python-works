# write a program to calculate monthly emi
# loan_amount
# tenture
# intrest_rate

p = float(input("Enter principle amount: "))
R = float(input("Enter annual interest rate: "))
n = int(input("Enter number of months: " ))

# Calculating interest rate per month
r = R/(12*100)

# Calculating Equated Monthly Installment (EMI)
emi = p * r * ((1+r)**n)/((1+r)**n - 1)

print("Monthly EMI = ", emi)


#total payable amount
total_payable_amount=emi *n
print("Monthly EMI:{emi}")
print(f"total_payable_amount={total_payable_amount}")

#total interest payable
total_interest_payable=total_payable_amount-p
print(f"total_interest_payable_amount={total_interest_payable}")