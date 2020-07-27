#  파이선 예제 연습 2주차

# 1. 입력을 정수 n 으로 받았을 때, n 이하 까지의 피보나치 수열을 출력하는 함수를 작성하세요.

n = int(input('정수 n을 입력하세요: '))
a = [1,1]
i=2
if n == 1:
    print(a[0])
if n == 2:
    print(a[:2])
if n >2 :
    while i < n :
        a.append(a[i-2]+a[i-1])
        i = i + 1
    print(a)

# 2. 사용자로부터 주민등록번호를 입력 받아 출생 연도를 출력하세요.

id_num = input('주민등록번호를 입력하세요: ')
if id_num[6] == '1' or id_num[6] == '2':
   print('19' + id_num[:2]+'생 입니다.')
if id_num[6] == '3' or id_num[6] == '4':
   print('출생연도는 20' + id_num[:2]+'생 입니다.')

#3. 연도가 주어졌을 때 윤 년이면 1, 아니면 0을 출력하는 프로그램을 작성하세요.
#	-윤년 = 연도가 4의 배수이면서 100의 배수가 아닐 때 또는 400의 배수일 때)

year = int(input('연도를 입력하세요.:'))
print(year)
if year % 4 == 0 and year % 100 != 0:
    print('1')
elif year % 400 == 0:
    print('1')
else:
    print('0')

# 4. 1부터 100 사이의 숫자를 하나 랜덤하게 생성하고, 이를 맞추는 게임을 작성하세요.
#	-숫자를 하나 생성하고, 그 다음 사용자가 숫자를 입력하면 이 둘을 비교하여 ‘높음’, ‘낮음’, ‘맞췄다’를 출력해야 한다.
#	-또한, 몇 번의 guess 끝에 답을 맞췄는지 시도한 횟수를 값으로 출력해야한다

import random

n = random.randint(1,100)
try_guess = 1
finish = True
while finish:
    guess = int(input('숫자를 맞춰 보세요.:'))
    print('시도 횟수 : ' +str(try_guess))
    if guess == n:
        print('맞췄습니다.')
        finish = False
    elif guess > n:
        print('더 낮은 숫자를 입력하세요.')
        try_guess = try_guess + 1
    else:
        print('더 높은 숫자를 입력하세요.')
        try_guess = try_guess + 1

# 5. 사용자로부터 달러 또는 위안 금액을 입력 받은 후 이를 원으로 환산해라.
#	-사용자는 100 달러, 100 위안 과 같이 금액과 통화 명 사이에 공백을 넣어 입력 하기로 합니다.
#	-각 통화 별 환율: 달러 :1112원, 위안: 171원

Money = str(input('금액을 입력하세요.:'))
i = 0
while i <len(Money):
    if Money[i] != ' ':
        i = i + 1
    else:
        break
Money_num = int("".join(Money[0:i]))
Money_unit = "". join(Money[i+1:])
if Money_unit == '달러':
    Exchage = Money_num * 1112
    print('달러 -> 원 : '+str(Exchage)+ '원')
if Money_unit == '위안':
    Exchage = Money_num * 171
    print('위안 -> 원 : '+str(Exchage)+ '원')

#  6. 로또번호 6개를 무작위로 생성하세요(1~45)(중복x)
import random
i = 0
j = 0
cnt = 0
lotto =[]
while i < 6 :
    n = random.randint(1,45)
    lotto.append(n)
    lenght = len(lotto)
    while j < lenght:
        if i == j:
            j = j + 1
        elif lotto[i] == lotto[j] :
            del lotto[i]
            break
        else:
            j = j +1
            cnt = cnt + 1
    if cnt == lenght-1:
        i = i +1
        j = 0
        cnt = 0
    else:
        j = 0
        cnt = 0
print(lotto)

# 7. 점수를 입력 했을 때 저수가 85점 이상이면 합격, 이하면 불합격이 나오게 작성하세요.
d = int(input('점수를 입력하세요. : '))
if d >= 85:
    print('합격입니다.')
else:
    print('불합격입니다.')

# 8. 별찍기. *로 입력한 숫자만큼 높이가 n인 삼각형을 출력하세요.
n = int(input('양의 정수 n을 입력하세요..:'))
i = 0
cnt = 1
j = n - cnt
while i < n :
    while j < n and j>=0:
        print('*', end='')
        j = j+1
    print('\n')
    cnt = cnt + 1
    j = j - cnt
    i = i +1
# 9. 전화번호를 입력받을 때 뒤에 4자리를 제외하고는 *로 가려지게 작성하세요.
PN = str(input('전화번호를 입력하세요. : '))
n=len(PN)
i = 0
PN = ','.join(PN)
PN = PN.split(',') 

while i < n-4:
    if PN[i] != '-':
        del PN[i]
        PN.insert(i,'*')
        i = i +1
    else:
        i = i + 1
print(''.join(PN))
# replace 로 바꾼 코드
PN = "010-7764-9954"
i = 0

n= int(len(PN))
while i < n-4:
    if PN[i] != '-':
        PN_re = PN.replace(PN[i],'*',1)
        i = i +1
        PN = PN_re
    else:
        i = i + 1
print(PN_re)

# 10. 리스트 a=[1,1,1,1,2,2,3,3,3,4,4,5,5,5]에서 중복 숫자를 제거한 [1,2,3,4,5] 리스트를 만드세요.

list_a=[1,1,1,1,2,2,3,3,3,4,4,5,5,5]
my_set = set(list_a)
my_list = list(my_set)

print(my_list)




