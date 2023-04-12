import requests

global x
x = 0

class ActionHelloWorld():
    global x
    x = 10 * 2
    print(x)

class ActionWelcome():
    global x
    print(x)



from datetime import datetime

fromdatevalue = '05/04/23'
todatevalue = '6/24/23'

try:
    # Convert date strings to datetime objects
    fromdate = datetime.strptime(fromdatevalue, '%d/%m/%y')
    todate = datetime.strptime(todatevalue, '%d/%m/%y')
except ValueError:  # catch block for ValueError exception
    print("Invalid date format!")
else:  # code to execute if no exceptions are caught
    # Convert datetime objects back to strings in the desired format
    fromdatevalue = fromdate.strftime('%Y-%m-%d')
    todatevalue = todate.strftime('%Y-%m-%d')

    print(fromdatevalue)
    print(todatevalue)

