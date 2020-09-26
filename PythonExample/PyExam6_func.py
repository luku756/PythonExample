
#기본 함수유형
def add(a,b):
    return a+b

result = add(1,3)
print(result)

result = add(b=3,a=1)
print(result)

print("")

#인자의 수가 미정인 함수
#입력을 모두 모아서 튜플로 사용.
def add_many(*args):
    print(args)
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1))
print(add_many(1,2))
print(add_many(1,2,2))
print(add_many(1,2,4,56,2,5,2))
print(add_many(1,2,4,56,2,5,2.4))
#print(add_many(1, "asd"))


print("")

#정해진 값과 튜플 변수 혼합

def calculate(mode, *args):
    if mode == "add":
        result = 0
        for i in args:
            result = result + i
        return result
    elif mode == 'mul':
        result = 1
        for i in args:
            result = result * i
        return result
    else :
        return -1


print(calculate('add',1))
print(calculate('mul',1,2))
print(calculate('add',1,2,2))
print(calculate(1,2,2))
#print(add_many(1, "asd"))


print("")

#키워드 파라미터, 딕셔너리 형태로 전달됨.

def print_keywordArgument(**kwargs):
    print(kwargs)

print_keywordArgument(a=1)
print_keywordArgument(calculate=2, sdr='s')

#다수의 리턴 값
#튜플 형태로 묶어서 리턴됨. C에서 구조체 리턴과 유사

def add_mul (a,b):
    return a+b, a*b #튜플로 생성됨

print(add_mul(4,5))

#아래 방식으로 각각 나눠서 받을 수 있음
res1, res2 = add_mul(4,5)
print("res1 : {0}, res2 : {1}".format(res1,res2))

#함수 초기값
#초기값은 뒤쪽에 몰려 있어야 함

def test(name, age=10, gender='M'):
    print("name : {0}, age : {1}, gender : {2}".format(name,age,gender))
    
test("ak")
test("ak",56,'F')
test("ak",54)
test("ak", gender = 'F')

#전역변수

a = 10
def globalVar():
    global a #전역변수라고 선언하지 않으면 에러 발생.
    a = a + 1

globalVar()
print(a)

#람다 함수
add = lambda a,b : a+b
result = add(3,5)
print(result)
