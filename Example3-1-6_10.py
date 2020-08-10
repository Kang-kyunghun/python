# 6. 자연수 n을 입력 했을 때 124나라에서 사용하는 숫자로 바꾸세요.

n = int(input('자연수를 입력 하세요. : '))
print(n)
x = 1
country124 = []
n = n - 1
while x != 0:
    x = n // 3
    y = n % 3
    print(x)
    if y == 0 :
        country124.append('1')
    elif y == 1 :
        country124.append('2')
    elif y == 2 :
        country124.append('4')
    n = x - 1
country124 = country124[::-1] #뒤집기
print(''.join(country124))

# 7. 국가 전체 예산 M을 정하고, 4개 지방에서 요청하는 예산을 각 각 정한 후 국가예산 전체를 최대로 사용 할 수 있는 지방예산의 상한액을 정하시오.

M = 569
m = [130, 184, 127, 129]
print('총 국가 예산 : {}'.format(M))
print('지방예산\n지방1 : {}, 지방2 : {}, 지방3 : {}, 지방4: {}'.format(m[0],m[1],m[2],m[3]))
change=[]
limit = max(m)
while True:
    for x in m :
        if x >= limit:
            x = limit
        change.append(x)
    if sum(change) > M :
        limit -= 1
        change =[]
    else:
        break
print('책정된 지방예산 합 : '+str(sum(change)))
print('지방예산 상한액 : '+str(limit))

# 평균 값으로 풀이
M = int(input('국가 총 예산을 입력 하세요.: '))
m = [int(i) for i in input('지방예산을 입력하세요. : ').split()]
remain =[]
new =[]
i = 0
mean = M/len(m)

print(mean)
for i in m:
    if i < mean:
        remain.append(mean-i)
        new.append(i)
S = sum(remain)/(len(m)-len(new))
limit = int(mean+S)
print(mean,S)
while len(m) != len(new):
    new.append(limit)
print(new)
print('상한액: ',limit)

# 8. n개의 100이하의 자연수를 입력하고, 그 수들의 최소 공배수를 구하시오

prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
multiple=[]
temp =[]
cnt = []
cnt_g = []

num = [12, 15, 50, 99]
i = 0
#소인수분해 코드
for j in num :
    while i < len(prime) :
        if j% prime[i] == 0:
            temp.append(prime[i])
            j = j // prime[i] # 입력된 수를 소수를 나눈 몫을 다시 나눔
        else:
            i += 1 # 해당 소수로 더 이상 나눌 수 없으면 다음 소수로 넘어감
    multiple.append(temp) #각 수의 소인수분해 리스트를 리스트로 묶음
    temp = []
    i = 0
print(multiple)

#해당 수에서 각 소수가 얼마나 있는 카운트 즉, 60 =2^2*3*5 이므로 2:2개,3:1개:5:1개
for x in multiple:
    for y in prime:
        cnt.append(x.count(y))
    cnt_g.append(cnt)
    cnt = []
#각소수별로 재배열
regroup =[]
temp = []
z = 0
for x in range(0,len(prime)):
    for y in range(0, len(num)):
        z = cnt_g[y]
        temp.append(z[x])
    regroup.append(temp)
    temp = []
print(regroup)
#최소공배수 계산
i = 0
result = 1
for x in regroup:
    if max(x) != 0:
        print(prime[i],max(x))
        result = result * (prime[i]**max(x))
    else:
        result = result * 1
    i += 1
print(result)

# 9. 자연수 n을 입력하고, 자연수 n의 약수들의 총 합을 구하시오.

n = int(input())
div = []
for i in range(1,n+1):
    if n % i == 0:
        div.append(i)
print(div)
print(sum(div))

# 10. 자판기 알고리즘을 짜시오.

cnt = 1
change = 0
menu = {'종료' : 0, '조니워커블루' : 250, '바카디151' : 20, 'Hennessy_X.O' : 200, '글렌피딕_21y' : 300}
key = list(menu.keys())
value = list(menu.values())
money = input('금액을 입력하세요. : ')
while True :
    print('원하시는 매뉴의 번호를 입력하세요.')
    n = int(input('1.조니워커블루 2.바카디151 3.Hennessy X.O 4.글렌피딕 21y : '))
    choice_manu = key[n]
    choice_value = value[n]
    change = int(money) - choice_value
    if change < 0 :
        print('금액이 부족 합니다. 잔돈 : '+str(money))
        break
    money = change
    print('잔돈 : {}, 이용횟수 : {}'.format(change, cnt))
    if cnt < 3 : 
        i = str(input('추가 구매 하시겠습니까?(Y/N) : '))
        if i == 'Y':
            cnt += 1
            continue
        else:
            print('잔돈 : ' +str(change))
            break
    else :
        print('이용횟수 초과!! 잔돈 : ' +str(change))
        break