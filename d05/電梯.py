import time
now=1
print('有一棟7層大樓的電梯系統,運作如下:')
print('您現在在1樓。請問要去哪樓?')
def total(now):
    def up(now, want):
        time.sleep(1)
        now=now+1
        print(now)
        if now==want:
            print('您現在在%d樓。請問要去哪一樓' % now)
        else:
            up(now, want)
    def down(now, want):
        time.sleep(1)
        now=now-1
        print(now)
        if now==want:
            print('您現在在%d樓。請問要去哪一樓' % now)
        else:
            down(now, want)





    want=int(input('>>'))
    if (want > now):
        time.sleep(1)
        now = now + 1
        print(now)
        if now == want:
            print('您現在在%d樓。請問要去哪一樓' % now)

    if (want < now):
        time.sleep(1)
        now = now - 1
        print(now)
        if now == want:
            print('您現在在%d樓。請問要去哪一樓' % now)

    total(now)
total(now)




