def proof():
    print("welcome to the even odd proof calculator")
    num = int(input('please enter your number'))
    if num % 2 == 0:
        print("Proof:")
        print("Notice that" + ' ' + str(num) + "" + "= 2n for all n in Integers")
        print("n = " + ' ' + str((num/2)) + ' ' + 'and n = ' + str((num/2)) + ' ' + 'is an integer')
        print("therefore, by definition of even number" + ' ' + str(num) + ' ' + 'is an even number since' + ' ' + str(num) + ' ' + '= 2n where all n belongs to integer')
    else:
        x = (num-1)/2
        print("Proof:")
        print("Notice that" + ' ' + str(num) + "" + "= 2n + 1 for all n in Integers")
        print("n = " + ' ' + '2(' + str(x) + ")+ 1" +' ' + 'and n = ' + str(x) + ' ' + 'is an integer')
        print("therefore, by definition of odd number" + ' ' + str(num) + ' ' + 'is an odd number since' + ' ' + str(num) + ' ' + '= 2n + 1 where all n belongs to integer')
    print('do you want to use this math proof calculator again')
    opt = ["1-yes","2-no"]
    for y in opt:
        print(y)
    playagain = int(input("enter your choice from the options above"))
    if playagain == 1:
        proof()
    elif playagain == 2:
        print("thanks for using this proof calculator")
    else:
        print("the option is not available, back to main menu")
        proof()
proof()