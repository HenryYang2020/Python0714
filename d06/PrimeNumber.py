#判斷是否是質數
def isPrime(n):
    bool=True  # 假設是質數
    for i in range(2, n//2+1):  # begin(含) end(不含)
        if 13 % i ==0:
            bool=False
            print('因數', i)
            break
    return bool
print(n, '質數' if bool else '不是質數')