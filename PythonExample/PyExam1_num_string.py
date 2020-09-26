"""
숫자와 문자열
"""

#엔터대신 공백으로 마무리.
print("asd", end=" ")
print("qwe", end=" ")

a = int( 17/2)#파이썬에서는 그냥 나누면 소수로 자동 캐스팅. 8.5
print(a)
#print(a+"asd") # 타입 에러 발생. a가 문자열이 아님
print(str(a)+"asd") #캐스팅 필요

print(17//2) # 17을 2로 나눈 몫
print(2**4) # 2^4

b = "asda"

print(b)
#b[2] = 't' //파이선은 문자열 수정을 허락하지 않음.
print(b)

c = '''
AS
ASD
ASDASD'''
print(c*3)
print(len(c))
print(len(c*3))
print("hello world"[-3])
print("hello world"[2:6]) #2<= < 6

#printf와 같은 사용방식. formatting. %s는 모든 타입을 받아 문자열로 변환
sk = "this is %d times %s taste good" % (3, "apple" )
print(sk)

# 0으로 채우기, 왼쪽정렬, 오른쪽정렬
sk = "this is %05d times %-10s taste %10s" % (3, "apple" ,"good" )
print(sk)

#함수 사용해서 정렬. 인덱스와 id 혼용가능. 정렬은 책 참조.
sk = "this is {0} times %{1} taste {laststr}" .format(3, "apple" ,laststr="good" )
print(sk)

#3.6 이상에서 사용 가능한 출력. 배열이나 딕셔너리 등도 사용 가능.
name = "홍길동"
age = 30
sk = f"이름 {name}, 나이 {age+1}"
print(sk)

"""
문자열 함수
count('c') - 포함된 수 세기
find() -- 처음 나온 위치(인덱스), 없으면 -1
index() - 문자열에서는 find 하위호환. 리스트를 위한 함수
upper()
lower()
lstrip()  -왼공백지우기
rstrip() - 오른공백지우기
strip() - 양공백지우기\
replace(target, str) - target을 str로 치환
"""

#모든 값 사이에 구겨넣기
sk = ", ,".join('abcd')
print(sk)

#쪼개기
sk = "a : b : c : d"
print(sk.split())#공백기준 나누기
print(sk.split(':'))#단위 기준 나누기. 단위만 제거됨
print(sk.split(' : '))#단위 기준 나누기