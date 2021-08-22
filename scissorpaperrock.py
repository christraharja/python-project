import random
def play():
    thelist = ['scissor','paper','rock']
    for k in thelist:
        print(k)
    user = str(input('please enter your choice from those three options above'))
    system = random.choice(thelist)
    system = str(system)
    global score
    score = 0
    print('your answer is' + ' ' + user + ' ' + 'and the computer answer is' + ' ' + system)
    if user == 'scissor' and system == 'scissor':
        res = 'draw'
        print(res)
        score = score
    elif user == 'scissor' and system == 'paper':
        res = 'won'
        print(res)
        score = score + 1
    elif user == 'scissor' and system == 'rock':
        res = 'lost'
        print(res)
        score = score - 1
    elif user == 'paper' and system == 'paper':
        res = 'draw'
        print(res)
        score = score
    elif user == 'paper' and system == 'rock':
        res = 'won'
        print(res)
        score = score + 1
    elif user == 'paper' and system == 'scissor':
        res = 'lost'
        print(res)
        score = score - 1
    elif user == 'rock' and system == 'rock':
        res = 'draw'
        print(res)
        score = score
    elif user == 'rock' and system == 'scissor':
        res = 'won'
        print(res)
        score = score + 1
    elif user == 'rock' and system == 'paper':
        res = 'lost'
        print(res)
        score = score - 1
    else:
        print('the option is not avaiable')
        play()
    print('your current score is' + ' ' + str(score))
    print('do you want to play again, enter 1 for yes and 2 for no')
    enter = int(input('enter your answer'))
    if enter == 1:
        print('enjoy the game')
        play()
    elif enter == 2:
        print('thanks for playing the game')
    else:
        print('the option is not available, back to main menu')
        play()
print('welcome to scissors paper rock game')
play()