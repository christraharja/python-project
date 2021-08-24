import math
import random
def game(level):
    s = 0
    num1 = random.randint(1,level)
    num2 = random.randint(1,level)
    num3 = random.randint(1,3)
    listop = ['+','-','*','/']
    opt = random.choice(listop)
    print(str(num1) + ' ' + str(opt) + ' ' + str(num2) + ' ' + ':')
    answer = float(input('enter your answer'))
    if opt == '+':
        if answer == num1 + num2:
            print('correct')
            s = s + 1
        else:
            print('wrong')
            s = s - 1
    elif opt == '-':
        if answer == num1 - num2:
            print('correct')
            s = s + 1
        else:
            print('wrong')
            s = s - 1
    elif opt == '*':
        if answer == num1 * num2:
            print('correct')
            s = s + 1
        else:
            print('wrong')
            s = s - 1
    elif opt == ":":
        if answer == num1 / num2:
            print('correct')
            s = s + 1
        else:
            print('wrong')
            s = s - 1
    print('your score = ' + ' ' + str(s))
def gauss(level):
    print('welcome to the gauss game')
    score = 0
    num = random.randint(1,level)
    print('1 + ... +' + ' ' + str(num) + ' ' + '=')
    theanswer = int(input('enter your answer'))
    if theanswer == (num * (num + 1))/2:
        print(str(theanswer)+ ' ' + 'is correct')
        score = score + 1
    else:
        print('wrong')
        score = score - 1
    print('your score = ' + ' ' + str(score))
def main():
    print("welcome to the fun math games")
    print('what games do you want to play')
    gamelist = ['1 - fast math','2-gauss']
    for e in gamelist:
        print(e)
    userinput = int(input("enter your choice here"))
    if userinput == 1:
        print('what level you want to play')
        listopt1 = ['1-beginner','2-intermediate','3-expert']
        for b in listopt1:
            print(b)
        user = int(input('enter your answer here'))
        time = int(input('how many times do you want to play'))
        if user == 1:
            for z in range(time):
                game(10)
        elif user == 2:
            for z in range(time):
                game(30)
        elif user == 3:
            for z in range(time):
                game(90)
        else:
            print('option is unavailable, go back to the main')
            main()
    elif userinput == 2:
        print('what level do you want to play')
        listopt2 = ['1-easy','2-hard']
        for g in listopt2:
            print(g)
        what = int(input('enter your answer here'))
        howmany = int(input('how many times do you want you play'))
        if what == 1:
            for i in range(howmany):
                gauss(10)
        elif what == 2:
            for i in range(howmany):
                gauss(60)
        else:
            print('option is unavailable, go back to the main')
            main() 
    print('do you still want to play, 1-yes or 2-no')
    ans = int(input('enter your answer here'))
    if ans == 1:
        main()
    else:
        print('thanks for playing this game')
main()
