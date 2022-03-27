import random

Dat = []
i, n = 0, 0

## 2017038093  김동민

if __name__ =="__main__" :
    for i in range(0, 5) :
        tmp = hex(random.randrange(0,100000))
        Dat.append(tmp)

    print ('정렬 전 데이터 : ', end = ' ')
    [print(num, end =' ') for num in Dat]

    for i in range(0, len(Dat)-1) :
        for n in range(i+ 1, len(Dat)) :
            if int(Dat[i], 16) > int(Dat[n], 16) :
                tmp = Dat[i]
                Dat[i] = Dat[n]
                Dat[n] = tmp
    print('\n정렬후 데이터 : ', end = ' ')
    [print(num, end =' ') for num in Dat]
