"""
변수 정보
"""

#단순 int일 때
a= 6
print(id(a)) #a의 주소값

b = a
print(id(b)) #b의 주소값
print(a is b) # 두 변수의 주소값이 동일한지 확인, TURE

#list일 때
a= [1,2,3]
print(id(a)) #a의 주소값

b = a
print(id(b)) #b의 주소값
print(a is b) # 두 변수의 주소값이 동일한지 확인, TURE

#값만 카피
b = a[:] #전체  데이터 슬라이싱
print(id(a)) #a의 주소값
print(id(b)) #b의 주소값
print(a is b) # 두 변수의 주소값이 동일한지 확인, false


#카피 함수를 추가
from copy import copy
b = copy(a) #카피 함수 사용
print(id(a)) #a의 주소값
print(id(b)) #b의 주소값
print(a is b) # 두 변수의 주소값이 동일한지 확인, false

a= 6
b = copy(a) #카피 함수 사용, 단순 변수면 대입으로 사용.
print(id(a)) #a의 주소값
print(id(b)) #b의 주소값
print(a is b) # 두 변수의 주소값이 동일한지 확인, true

#값 대입
a,b = (6,14)
print("a : {0}, b : {1}".format(a,b))

[a,b] = ["asdasd", 36.8]
print("a : {0}, b : {1}".format(a,b))

(a,b) = 3737, "kKk"
print("a : {0}, b : {1}".format(a,b))

a = b = (6,14)
print("a : {0}, b : {1}".format(a,b))

#값 swap
a=3
b=5
print("a : {0}, b : {1}".format(a,b))
a,b = b,a
print("a : {0}, b : {1}".format(a,b))