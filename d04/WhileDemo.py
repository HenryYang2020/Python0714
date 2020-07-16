import random

while True:
    n=random.randint(1, 100)
    if n%3==0:
        print(n)
        continue#直接重複執行迴圈
    #若n等於11的倍數就停止(break)
    if n %11==0:
        break
