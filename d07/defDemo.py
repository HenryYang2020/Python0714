def calc(x=0, y=0) ->int :
    return x+y

def calc2(x=None, y=None) ->int :
    if x==None:
        print('使用者沒帶入x值')
    if y==None:
        print('使用者沒帶入y值')
    return x+y

if __name__ == '__main__':
    sum = calc(10, 20)
    print(sum)
    sum = calc()
    print(sum)

