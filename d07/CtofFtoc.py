
def ctof(c) ->float :
    f = c*(9/5)+32
    print(f)
def ftoc(f) ->float :
    c = (f-32)*5/9
    print(c)
choice = input('1:攝氏to華氏 2:華氏to攝氏')
if choice == 1:
    c = input('請輸入溫度(C)')
    ctof(c)
