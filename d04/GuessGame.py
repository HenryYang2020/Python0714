
import random
ans=(random.randint(1,99))
min, max = 0, 100
while True:
    guess = int(input('請在%d~%d之間猜一數字:' % (min, max)))
    if(guess > ans and guess<100):
        max = guess
    elif (guess <ans and guess<100):
        min = guess
    elif ans==guess:
        print('恭喜答對')
    else :
        print('肏你媽')


