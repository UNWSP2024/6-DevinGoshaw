# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:
#programmer:Devin Goshaw
#date:10/7/25
#program: total tax program
def tax():
    totalsales=float(input('what are your total sales for the month in dollars:'))
    countrytax=.05*totalsales
    statetax=0.025*totalsales
    print('The country tax is:$',countrytax)
    print('the state tax is:$',statetax)
    totaltax=countrytax+statetax
    print('the total tax is:$', totaltax)
    total=totalsales+countrytax+statetax
    print('the grand total is:$',total)
    return countrytax, statetax, totalsales
tax()
# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program