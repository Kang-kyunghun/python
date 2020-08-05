#구구단
def ex_while():
    i=2
    j=1
    while i<10:
        while j<10:
            print('{} X {} = {}'.format(i, j, i*j))
            j += 1
        j = 1
        i += 1

def ex_for():
    for i in range(2,10):
        for j in range(1,10):
            print('{} X {} = {}'.format(i, j, i*j))

def ex_break():
    n = 2
    loof = True
    while loof :
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        n +=1 # 이거 위치가 continue랑 다름
        con=input(str(n)+'단을 출력하시겠습니까?(Y/N) : ')
        if con == 'N':
            break
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        loof = False
    print('구구단이 종료 되었습니다.')

def ex_continue():
    n = 2
    loof = True
    while loof :
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        con=input(str(n)+'단을 다시 출력하시겠습니까?(Y/N) : ')
        if con == 'Y':
            continue
        n += 1
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        loof = False
    print('구구단이 종료 되었습니다.')

#ex_while()
#ex_for()
#ex_break()
#ex_continue()

#전부 return이 없는 함수