#Easy Financial Allocator

from constants import SPEND_RATE, SAVE_RATE, BONDS_RATE, INVEST_RATE, IRA_RATE
from constants import PSTRINGS
from ratios import ratioCalc
income = float(input("Input your income amount: "))

def easyAllocate():
    print("Spend:" + str(income * SPEND_RATE))
    print("Save:" + str(income * SAVE_RATE))
    print("Bonds:" + str(income * BONDS_RATE))
    print("Stocks:" + str(income * INVEST_RATE))
    print("Roth IRA:" + str(income * IRA_RATE))


def designateIncome(dollars_change_needed):
    sums = 0
    for b in range(len(dollars_change_needed)):
        if dollars_change_needed[b] < 0:
            dollars_change_needed[b] = 0
        
    for c in dollars_change_needed:
        sums = sums + c
    
    print("\nWeighted Income Allocation for This Check:")
    for d in range(len(dollars_change_needed)):
        print(PSTRINGS[d]+"$"+str(round(
            dollars_change_needed[d]/sums*income,2)))

dollars_change_needed = ratioCalc()

designateIncome(dollars_change_needed)


