import math
print('welcome to the online banking system')
def signin():
    global name
    global pin
    global cb
    name = str(input('please create your username'))
    pin = str(input('please create your 6 digits pin'))
    if len(pin) == 6:
        pin = pin
    else:
        print('the pin has to be in 6 digits')
        newpin = str(input('please create your 6 digits pin'))
        if len(newpin) != 6:
            print('the pin has to be in 6 digits and your trial is done')
        else:
            newpin = pin
    print('thanks for creating your account')
def forgotpin():
    recoverpin = str(input('please create your 6 digits pin'))
    if len(recoverpin) == 6:
        recoverpin = pin
    else:
        print('the pin has to be in 6 digits')
        recoverpin = str(input('please create your 6 digits pin'))
        if len(recoverpin) != 6:
            print('the pin has to be in 6 digits and your trial is done')
        else:
            recoverpin = pin
            # login again 
            login()
def depositinterest(p,r,t):
    # A = pe^(rt) is the formula to calculate the compound interest rate
    p = float(p)
    r = float(r)
    t = float(t)
    a = p * math.exp(r * t)
    return a
def login():
    name1 = str(input('please enter your username'))
    pin1 = str(input('please enter your pin'))
    if name1 == name and pin1 == pin:
        print('welcome to the online banking system' + ' ' + name)
        print('please choose the menu downhere')
        menu = list()
        menu = ['1-deposit','2-withdraw','3-transfer','4-check balance','5-deposit interest rate','6-calculate compound interest']
        for y in menu:
            print(y)
        choose = int(input("please enter the number provided above"))
        d = 0
        w = 0
        cb = 0
        if choose == 1:
           d = int(input('enter the amount of your deposit'))
           cb = d
           print('your current balance is' + ' ' + str(cb))
        elif choose == 2:
            w = int(input('enter the amount of your withdrawal'))
            if w > cb:
                print('your current balance is not available for transaction')
            else:
                cb = d - w
                print(str(w) + ' '+ 'has been withdrawn from your account' + ' ' + 'and your current balance is' + str(cb))
        elif choose == 3:
            dest = str(input('please enter the account number of your destination in 8 digits'))
            if len(dest) == 8:
                amount = int(input('please enter the amount of money you want to transfer'))
                if amount > cb:
                    print('your current balance is not available for transaction')
                else:
                    cb = d - amt
                    print('the transaction of' + ' ' + str(amt) + ' ' + 'has been transferred to' + ' ' + str(dest) + ' ' + 'your current balance is' + str(cb))
            else:
                print('the transaction has been rejected since the destiantion account number is invalid')
        elif choose == 4:
                print('your current balance is' + ' ' + str(cb))
        elif choose == 5:
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate = 2
            else:
                rate = 1.5
            print('your current deposit interest rate is'+ ' ' + str(rate) + ' %')
        elif choose == 6:
            listc = ["1-calculate your deposit compound interest based on your current balance",'2- calculate your deposit compound interest based on your deposit input']
            for ijk in listc:
                print(ijk)
            choice = int(input('please enter your choice from the options above'))
            if choice == 1:
                timing = str(input('please enter how many years you want to calculate'))
                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print('your current balance in' + ' ' + timing + ' '+'years will be')
                print(depositinterest(cb,ratex,timing))
            elif choice == 2:
                timing1 = str(input('please enter how many years you want to calculate'))
                money = str(input('please enter the amount of money in your current balance which you would like to caclulate'))
                money = int(money)
                if money > 50000:
                    rate1 = 3/100
                elif money > 30000:
                    rate1 = 2/100
                else:
                    rate1 = 1.5/100
                print('your current balance in' + ' ' + timing1 + ' '+'years will be')
                print(depositinterest(money,rate1,timing1))
        else:
            print('option is not available, back to the main menu')
            login()
    else:
        print('your username or password is wrong, did you create your account?')
        list1 = ["1-yes","2-no"]
        for b in list1:
            print(b)
        inp = int(input('enter your choice below'))
        if inp == 1:
            list2 = ['1-do you want to attempt to log in again','2-forget pin']
            for e in list2:
                print(e)
            theanswer = str(input('please enter your choice'))
            theanswer = int(theanswer)
            if theanswer == 1:
                login()
            elif theanswer == 2:
                print('forget pin, please reset your pin')
                forgotpin()
            else:
                print('option is not abvailable')
        elif inp == 2:
            print('please create your account')
            signin()
option1 = int(input('please choose 1 to sign in and 2 to log in'))
if option1 == 1:
    signin()
elif option1 == 2:
    login()
else:
    print('option is unavailable')
option2 = int(input('please choose 1 to sign in and 2 to log in'))
if option2 == 1:
    signin()
elif option2 == 2:
    login()
else:
    print('option is unavailable')
print('thanks for the transaction, do you still want to make another transaction?')
opt = ["1 for yes","2 for no"]
for x in opt:
    print(x)
ans = int(input('please enter your answer'))
if ans == 1:
    login()
elif ans == 2:
    print('thanks for using this online banking system')
else:
    print('option is unavailable')