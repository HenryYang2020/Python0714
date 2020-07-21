import statistics
import random

scores=[]
for i in range(0,10):
    scores.append(random.randint(0,10))


def getStat(list):
    # 排序
    scores.sort()
    # 移除最小的2個原素
    # __delitem__(0)移除第0個元素
    # remove(0)移除是0的資料
    scores.__delitem__(0)
    scores.__delitem__(0)
    print(scores)
    # 移除最大的2個元素
    scores.__delitem__(len(scores) - 1)
    scores.__delitem__(len(scores) - 1)
    print(scores)

    mean = statistics.mean(scores)
    print('平均', mean)

    stdev = statistics.stdev(scores)
    print('標準差:', stdev)

    cv = stdev / mean
    return stdev, mean, cv
a, b = [], []
for i in range(0, 10):
    a.append(random.randint(0, 10))
    b.append(random.randint(0, 10))

print(a)
print(b)

mean_a, stdev_a, cv_a = getStat(a)
mean_b, stdev_b, cv_b = getStat(b)
print(mean_a, stdev_a, cv_a)
print(mean_b, stdev_b, cv_b)

