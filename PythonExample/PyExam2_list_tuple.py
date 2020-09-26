"""
리스트 : vector + list + a
"""
a = []
b = list()

c = [1, 2, 34, 12.5]
d = ["asd", 12 , 5.7, [123, "sdf", c, "sdfs", a]]

print(c)
print(d)
del d[1] # 12 가 사라짐
print(d)

#a 에 값 추가
a = []
a.append(3)

#더하기 연산으로 뒤에 이어붙이기 가능
b = [1,2]
a += b
print(a) #3,1,2

d = ["asd", 12 , 5.7, [123, "sdf", c, "sdfs", a]]
del d[1:3] # 12, 5.7  사라짐
print(d)

#size 크기만큼 초기화
lists = [0 for i in range(size)]

#리스트 정렬 방식. 람다 함수를 써서 원하는 조건으로 정렬. 아래는 역순(내림차순, 큰거 앞으로) 정렬.
#arr의 각 값을 play라는 리스트에 집어넣어서 그 값을 기준으로 정렬한 것. 사용 나름
arr.sort(key = lambda x : plays[x], reverse=True)

"""
인덱싱, 슬라이싱 사용 가능.
 d[2:4], c[2] 등 
 
 더하기, 곱하기(반복) 가능

appand - push_back
insert - 중간에 삽입
remove - 중간을 제거
pop() - 마지막 값을 리턴하고 제거
pop(id) - index id 값을 리턴하고 제거
count() - 동일한 값의 수 확인하여 개수 리턴
sort() - 오름차순 정렬
sort(reverse=True) - 내림차순 정렬
sort(key=len) - key에 지정된 함수의 결과에 따라 정렬. 이 경우 문자열 리스트 정렬
reverse
index - 있으면 위치 리턴. 없으면 에러
"""


'''
튜플 : ()
값의 삭제, 수정, 생성 불가능
'''

t1 = ()
t2 = (1,)
t3 = (2)    #튜플이 아님, 반드시 , 필요
t4 = (1,2,3)
t5 = 1,2,3
t6 = ('a','b',(1,2))
t7 = ('a',2,(1,2,'c'))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)