data = '170,60&160,48'

for row in data.split('&'):
    print(row, type(row))
    h,w = row.split(',')
    bmi='%.2f'%float(w)/(float)