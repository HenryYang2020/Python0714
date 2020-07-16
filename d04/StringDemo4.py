report = '台積電每股315.5元,可賣出4000股,目前我的庫存有6000股'
# 求賣出後的庫存總值
price=float(report[5:10])
sell=int(report[15:19])
all=int(report[28:32])
print(price, sell, all)
print((all-sell)*price)