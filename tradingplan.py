import math
def regulartrading():
    print('regular trading plan')
    deposit = float(input('please enter your initial deposit'))
    profit = float(input('please enter the profit in decimals'))
    time = int(input('please enter the amount of trade'))
    estimation = deposit * profit * time
    print('your estimated profit will be' + ' ' + str(estimation))
def compoundinteresttrading():
    print('compound interest trading plan')
    deposit = float(input('please enter your initial deposit'))
    profit = float(input('please enter the profit in decimals'))
    time = int(input('please enter the amount of trade'))
    estimation = deposit * (profit**time)
    print("your estimated total profit will be" + ' ' + str(estimation))
def safetrade():
    print('please input your level')
    listopts = ['1-beginner','2-medium','3-expert']
    for p in listopts:
        print(p)
    answer = int(input('please enter your level'))
    amt = float(input('please enter your current balance'))
    if answer == 1:
        safe = amt * 1/100
        print('for safety, please trade with no more than' + ' ' + str(safe))
    elif answer == 2:
        safe = amt * 3/100
        print('for safety, please trade with no more than' + ' ' + str(safe))
    elif answer == 3:
        safe = amt * 5/100
        print('for safety, please trade with no more than' + ' ' + str(safe))
    else:
        print('the option is unavailable, back to main menu')
        safetrade()
def mainmenu():
    print('welcome to the trading plan system')
    print('please choose the menu below')
    listmenu = ['1-regular trading','2-compound interest trading','3=safetrade and risk management']
    for r in listmenu:
        print(r)
    choose = int(input('enter your choice here'))
    if choose == 1:
        regulartrading()
    elif choose == 2:
        compoundinteresttrading()
    elif choose == 3:
        safetrade()
    else:
        print('the option is currently unavailable, back to main menu')
        mainmenu()
    print('do you still want to use the app')
    choice = int(input('enter 1 for yes and 2 for no'))
    if choice == 1:
        mainmenu()
    elif choice == 2:
        print('thanks for using the app')
    else:
        print('the option is not available, back to main menu')
        mainmenu()
# call the mainmenu function
mainmenu()


