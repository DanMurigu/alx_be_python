monthly_income = int(input("Enter your monthly income: ")) #prompt the user to input their monthly income and convert to integer
monthly_expenses = int(input("Enter your total monthly expenses: ")) #prompt the user to input their monthly income and convert to integer
monthly_savings = monthly_income - monthly_expenses #calculates the users monthly saving
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) #calculates the projected annual saving assuming a 50% interest per month

print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",projected_savings)
