#43 함수
#  def 함수이름(인자1,...):
#     실행할 명령1
#     실행할 명령2
#     return 결과

#44 함수를 사용하는 이유
def add(num1, num2):
    return num1 + num2
a = add(1,2)
print(a)

#45 여러개 돌려주기
def add_mul(num1, num2):
    return num1 + num2, num1 * num2
b = add_mul(1, 2)
print(b)
my_add, my_mul = add_mul(1, 2)
print(my_add, my_mul)

#46 모듈
# 비슷한 함수들을 모아둔 파일
# 내가 모듈을 직접 만들거나 미리 만들어져 있는 모듈들을 가져와 쓸 수 있다.

#47 랜덤 random.choice(), random.sample(), random.randint()
import random
rus_roulette = [1, 2, 3, 4, 5, 6]
a = int(input('몇 번 쏘시겠습니까? :'))
cnt = a
for i in range(a):
    b = random.choice(rus_roulette)
    cnt -= 1
    if b % 2 == 0:
        print('{0}번 째.. bang!' .format(i+1))
        print('GAME OVER')
        break
    else:
        print('{0}번 째.. click!' .format(i+1))
        if cnt == 0:
            print('your alive!')
        else:
            print('...next')
        del rus_roulette[b]

print(random.sample(range(1, 46), 6))

print(random.randint(8, 10))

#48 객체

#49 코딩 스타일 (PEP8)
# 공적인 파이썬 작업을 할 때의 규칙
"멍청하게 일관성을 고집하는 것은 소인배의 발상이다."

#50 구글링 방법

