import random
import operator

def randomQuestion():
    operators = {"+": operator.add, "-": operator.sub,"*": operator.mul,"/": operator.truediv,}
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)
    o = random.choice(list(operators.keys()))
    answer = operators.get(o)(num1,num2)
    print(f'what is {num1} {o} {num2} ?')
    return  answer

def askQuestion():
    thecorrectanswer = randomQuestion()
    userguess = int(input())
    return userguess == thecorrectanswer

def theGame():
    print("Let's begin the math game!")
    s = 0
    for i in range(3):
        if askQuestion() == True:
            s = s + 1
            print("your answer is corect!")
        else:
            s = s - 1
            print("your answer is wrong!")
    print(f'Your total score is {s}')
theGame()




