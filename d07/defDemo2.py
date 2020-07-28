def calc(*score) -> int:
    print(type(score), score)
    sum=0;
    for s in score:
        sum += s
    return sum

if __name__ == '__name__':
    sum = calc(10, 20, 30, 40)
    print(sum)
    sum = calc()

