import operator

## 2017038093 김동민
train = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5),
          ('토마스', 4), ('헨리', 7), ('토마스', 3), ('에밀리', 8),
          ('퍼시', 5), ('고든', 13)]

traind, trainl = {}, []
tm =None
to, rank = 1, 1

if __name__ =="__main__" :
    for tm in train :
        tname = tm[0]
        tw = tm[1]
        if tname in traind :
            traind[tname] += tw
        else :
            traind[tname] = tw
            
    print('기차 수송량 목록 >>', train)
    print('--------------------------')
    trainl = sorted(traind.items(), key = operator.itemgetter(1),
                    reverse = True)

    print('기차\t총 수송량\t 순위')
    print('--------------------------')
    print(trainl[0][0], '\t', trainl[0][1], '\t', rank)
    for i in range(1, len(trainl)) :
        to += 1
        if trainl[i][1] == trainl[i-1][1] :
            pass
        else :
            rank = to
        print(trainl[i][0], '\t', trainl[i][1], '\t', rank)


