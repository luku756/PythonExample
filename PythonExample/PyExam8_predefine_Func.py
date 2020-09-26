
#include -> import 모듈이름 (확장자 제거, 파일명 쓰면 됨)
#사용 시 모듈이름.함수이름 으로 사용해야 함

#from 모듈이름 import 함수명

"""
#중에서 add만 사용
from mod1 import add

#모든 함수 사용
from mod1 import * 


"""


#지니고 있는 멤버함수 출력.
print (dir([1,2,3]))

#문자열 형식으로 함수 호출 등을 행하고 그 결과물을 리턴.
eval();

#func 에 반복 가능한 list 값을 넣어서 참인 것만 묶어서 리턴.
filter(func, list)


#func 에 반복 가능한 list 값을 넣어서 각각의 수행 결과물을 리스트로 리턴.
map(func, list)

#그 안에서 최대, 최소
max(), min()

sorted() #정렬 결과를 리턴해줌. sort는 리턴은 x

if __name__ == "__main__":
    ##내가 시작 파일일 때에만 적용.
    pass
