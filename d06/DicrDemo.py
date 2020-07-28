# 字典資料格式
fruits={'orange':20, 'apple':10, 'watermelon':30}
print('orange幾元', fruits.get('orange'))
print('apple幾元',fruits.get('apple'))
print('watermelon幾元',fruits.get('watermelon'))
print(fruits)
#setdefault(Key值,預設值(若找不到此元素)
print('banana 幾元', fruits.setdefault('banana',70))
print(fruits)
print('apple 幾元', fruits.setdefault('apple',100))
print(fruits)
#取得所有的key值
names=fruits.keys()
print(names, type(names))
#取得所有的Values值
values=fruits.values()
print(values, (sum=))