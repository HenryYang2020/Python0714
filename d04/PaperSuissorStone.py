import random
num=(random.randint(1, 3))

def win():
    print('你贏了')
def lose():
    print('你輸了')
def even():
    print('平手')
print('請輸入你要選擇的:')
print('剪刀or石頭or布')
aa=int(input('->'))
print('你的對手')
if num==1:
    print('剪刀')
elif num==2:
    print('石頭')
else:
    print('布')
print('你')
if aa==1:
    print('剪刀')
elif aa==2:
    print('石頭')
else:
    print('布')

if aa==num:
    even()
elif (aa==1, num==2):
    lose()
elif (aa==1, num==3):
    win()
elif (aa==2, num==3):
    lose()
elif (aa==2, num==1):
    win()
elif (aa==3, num==1):
    lose()
else:
    win()




