#雞兔同籠
# x雞 y兔
x = int(input("請輸入動物總數:"))
y = 0
z =int(input("請輸入一共幾隻腳:"))
def wan(x, y, z):
    if ((x*2)+(y*4))==z:
        print('%.1f隻雞 %.1f隻兔子'%(x, y))
    else:
        x=x-1
        y=y+1
        wan(x, y, z)
wan(x, y, z)