from matplotlib import pyplot as mp
from constants import PSTRINGS





def ratioCalc():
    from constants import RATE_ARRAY
    
    
    portfolio = [7500, 200, 1500, 2000] #[4,2,3,1]#
    #save bonds invest ira
    portfolio_ratios = []
    percent_change_needed = []
    dollars_change_needed = []
    
    
    
    total = portfolio[0]+portfolio[1]+portfolio[2]+portfolio[3]
    
    
    print("Current Allocation:")
    for x in range(len(portfolio)):
        portfolio_ratios.append(round(portfolio[x]/total*100, 2))
        print(PSTRINGS[x]+str(portfolio_ratios[x])+"%")
        
    pieRatios(portfolio_ratios)
        
    print("\nNeeded Change to Meet Desired Allocation:")    
        
    for y in range(len(portfolio_ratios)):
        percent_change_needed.append(
            round(RATE_ARRAY[y+1]*200 - portfolio_ratios[y]))
        print(PSTRINGS[y]+str(percent_change_needed[y])+"%")
    
    print("\nNeeded Change Dollar Amount:")
    for z in range(len(percent_change_needed)):
        dollars_change_needed.append(
            round(percent_change_needed[z]/100*total))
        print(PSTRINGS[z]+"$"+str(dollars_change_needed[z]))
        
    return dollars_change_needed
        
def pieRatios(pval):
    mp.pie(pval)
    mp.title("Portfolio Allocation")
    
