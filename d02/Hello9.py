#小明的身高是170cm體重是60kg BMI計算結果為 20.76(正常)
#__的身高是___cm體重是__kg BMI計算結果為 __.__(__)
print('BMI系統')
name=input('請輸入姓名:')
h=float(input('請輸入身高(cm):'))
w=float(input('請輸入體重(kg):'))
bmi=w/((h/100)**2)
result='正常' if 18<bmi <=23 else '過高' if bmi>23 else "過低"
print('%s的身高是%5.1fcm體重是%5.1fkg BMI計算結果為 %5.2f(%s)'
      %(name, h, w, bmi, result))





