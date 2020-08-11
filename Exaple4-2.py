# 1. 사이트의 비밀번호 만들기
#모범답안
#조건1 : http://을 없앤다.
#조건2 : 첫번째 '.'전까지만 남긴다.
#조건3 : 비밀번호 = 남은 문자열의 앞 3자리 + 남은 문자열의 길이 + 남은 문자열 중 'e'의 수 + '!'

url = "http://naver.com"
my_str = url.replace('http://', '')
my_str = my_str[:my_str.index('.')]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print("{}의 비밀번호는 {} 입니다.".format(url, password))


# 2. 당시는 kakao 서비스를 이용하는 택시 기사입니다. 50명의 승객과 매칭 기회가 있을 때, 아래 조건을 만족하는 승객 수를 구하시오.
# - 조건 1: 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다.
# - 조건 2: 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다.

from random import *

people = []

for x in range(1, 51):
    people.append(randint(5,50))
cnt = 0
n=1
for i in people:
    if 5 <= i <=15:
        print('[O] {}번째 손님 (소요시간: {})'.format(n,i))
        cnt += 1
    else:
        print('[X] {}번째 손님 (소요시간: {})'.format(n,i))
    n += 1
print(f'총 탑승 승객 수 : {cnt}')

#모범 답안
from random import *

cnt = 0
for i in range(1, 51):
    time = randrange(1, 51)
    if 5 <= time <= 15:
        print("[O] {}번째 손님 (소요시간 : {}분)".format(i, time))
        cnt += 1
    else:
        print("[X] {}번째 손님 (소요시간 : {}분)".format(i, time))
print("총 탑승 승객 : {} 분".format(cnt))


# 3. 한 클래스에 두 개의 객체(공격,방어)를 만들어 '캐릭터 싸움'을 구현해주세요.

from random import shuffle, randint
#class 생성
class CharaterFight():
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.hp = 100 #hp는 처음 100으로 고정
    def attack(self, enemy):
        enemy.hp = enemy.hp -10
    def defense(self):
        self.hp = self.hp - 5

#Kyunghun, Kyugman이라는 인스턴스 생성(이름, 직업 속성 부여)
Kyunghun = CharaterFight('Kyunghun', '법사')
Kyungman = CharaterFight('Kyungman', '전사')
#생성산 인스턴스들의 정보 출력
print(f'{Kyunghun.name}의 직업은 {Kyunghun.job}입니다.(hp: {Kyunghun.hp})')
print(f'{Kyungman.name}의 직업은 {Kyungman.job}입니다.(hp: {Kyungman.hp})')
print()

choice = [0, 1]
user = [Kyunghun, Kyungman]
while True:
    shuffle(choice)
    i = choice.pop()
    j = choice[0]
    if randint(0,1) :# i의 공격성공, j의 방어실패
        user[i].attack(user[j])
        print(f'{user[i].name}가 공격에 성공했습니다.')
        print(f'상대 {user[j].job}에게 -10의 피해를 입혔습니다.')
        print(f'남은 hp  Kyunghun: {Kyunghun.hp}, Kyunman: {Kyungman.hp}')
        print()
    else: #i의 공격, j의 방어성공
        user[j].defense()
        print(f'{user[j].name}가 방어에 성공했습니다.')
        print(f'{user[j].job}가 -5의 피해를 입었습니다.')
        print(f'남은 hp  Kyunghun: {Kyunghun.hp}, Kyunman: {Kyungman.hp}')
        print()
    if Kyunghun.hp <= 0:
        print('Kyugman이 승리 했습니다.')
        break
    elif Kyungman.hp <= 0:
        print('Kyunhun이 승리 했습니다.')
        break
    choice = [0, 1]

# 4. String형 배열 Seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, 
# solution을 완성하세요. Seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
# 예> Seoul = ['Jane', 'Kim'] 
# return "김서방은 1에 있다"

# - Seoul은 길이 1 이상, 1000 이하인 배열입니다.
# - Seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# - Kim은 반드시 Seoul 안에 포함되어 있습니다.

def find_kim(my_list):
    return print('김서방은 {}번째에 있다.'.format(my_list.index('Kim')))

Seoul = [x for x in input('값을 입력하세요. : ').split()]
#Seoul = ['Kang', 'Jang', 'Lee', 'Kim', 'Choi']
find_kim(Seoul)



# 5. 재귀함수를 활용하여 피보나치 수열을 만드시오.

def fibo(n):
    global cnt
    cnt += 1 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
cnt = 0       
n = int(input('0이상의 정수를 입력하세요.: '))
print(fibo(n), cnt)


#재귀함수의 문제점을 해결해주는 **메모화(memoization)
'''
메모 = { 1:1, 2:1 }
def fib(n):
    if n in 메모:
        return 메모[n]
    else:
        output = fib(n-1) + fib(n-2) #아웃풋이라는 변수에 저장
        메모[n] = output          # 한번 저장 했던 값이니까
        return output
print(fib(100))
'''
#**이는 한번 계산 했던 것은 다시 계산하지 않고, 메모 했던 것을 확인하기 때문이다
