#計算總分
def getSum(scores):
    # 求總分
    sum = 0
    for i in range(0, len(scores)):
        sum += scores[i]  # 累加
    return sum
#計算平均
def getAvg(scores):
    sum=getSum(scores)
    avg=sum/len(scores)
    return avg
#主程式
scores=[100,90,80,70,60]#數組
print(len(scores))
#各科列印
for i in range(0, len(scores)):
    print(scores[i])
#求總分
sum=getSum(scores)
print('總分: %d'%sum)

#求平均
avg=getAvg(scores)
print(sum/len(scores))