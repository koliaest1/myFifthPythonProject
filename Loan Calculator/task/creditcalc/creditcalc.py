import math
import argparse
# loan_principal: int = int(input("Enter the loan principal: "))
# calculation = input('''What do you want to calculate?
# type "m" - for number of monthly payments,
# type "p" - for the monthly payment:''')
# if calculation == "m":
#     monthly_payment = int(input("Enter the monthly payment: "))
#     months = math.ceil(loan_principal / monthly_payment)
#     lexeme = "month" if months == 1 else "months"
#     print("It will take " + str(months) + lexeme + " to repay the loan")
# else:
#     number_of_months = int(input("Enter the number of months: "))
#     monthly_calculation = math.ceil(loan_principal / number_of_months)
#     residual = loan_principal - (monthly_calculation * (number_of_months - 1))
#     if residual == 0:
#         print("Your monthly payment = " + str(monthly_calculation))
#     else:
#         print("Your monthly payment = " + str(monthly_calculation) + " and the last payment = " + str(residual))

parser = argparse.ArgumentParser()
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--type")
args = parser.parse_args()
if not args.interest or args.interest and args.interest < 0 or args.principal and args.principal < 0 or args.periods and args.periods < 0 or args.payment and args.payment < 0:
    print("Incorrect parameters")
else:
    interest = args.interest / (12 * 100)
    if args.type == "annuity":
        if not args.principal:
            principal = math.ceil((args.payment / ((interest * (1 + interest)** args.periods)/((1 + interest)**args.periods - 1))))
            print(f"Your loan principal = {principal}!")
        else:
            principal = args.principal
        if not args.payment:
            payment = math.ceil(principal * ((interest * (1 + interest)**args.periods)/((1 + interest)**args.periods - 1)))
            print(f"Your monthly payment = {payment}!")
        else:
            payment = args.payment
        if not args.periods:
            periods = math.log((payment / (payment - interest * principal)), (1 + interest))
            years = math.ceil(periods) // 12
            months = math.ceil(periods) % 12
            if years == 0:
                print(f"It will take {months} months to repay this loan!")
            else:
                if months == 0:
                    print(f"It will take {years} years to repay this loan!")
                else:
                    print(f"It will take {years} years and {months} months to repay this loan!")
        else:
            periods = args.periods
        overpayment = math.ceil(periods) * payment - principal
        print(f"Overpayment = {overpayment}")
    elif args.type == "diff":
        if not args.interest or not args.principal or not args.periods:
            print("Incorrect parameters")
        else:
            principal = args.principal
            interest = args.interest / (12 * 100)
            periods = args.periods
            total = 0
            for month in range(1, periods+1):
                payment = math.ceil((principal / periods) + interest * (principal - ((principal * (month - 1))/periods)))
                print(f"Month {month}: payment is {payment}")
                total += payment
            overpayment = total - principal
            print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters")
