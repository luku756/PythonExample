
"""
딕셔너리 - map을 생각하면 된다.
혹은 json obejct를 생각하자.
"""

a = {}
b = dict()

dic = {'name' : "홍길", 3 : 'asd', 10 : [1,2,3,4,{11:"a",12:'b',13:'c'}], "qwe" : 7}
print(dic)

#print(dic['3']) # 없는 키 참조시 에러
print(dic.get('3')) #없는 값 참조시 NONE 리턴
print(dic.get('3',0)) #디폴트 값 추가. 없으면 이거 리턴

print('3' in dic) #값 있는지 확인
print('name' in dic) #값 있는지 확인

#값 바꾸기
print( dic['name'])
dic['name'] = 1024
print( dic['name'])

#딕셔너리 키 사용
print( dic.keys())  #리스트 타입이 아님. [3]과 같이 접근 불가
print( list(dic.keys()))#리스트로 캐스팅
for k in dic.keys():
    print(k)

    
#딕셔너리 값 사용
print( dic.values())  #리스트 타입이 아님. [3]과 같이 접근 불가
for k in dic.values():
    print(k)

#전체 정보 얻기
print( dic.items())  #리스트 타입이 아님. [3]과 같이 접근 불가
for k in dic.items(): #순서쌍 출력
    print(k)

"""
clear() 모두 지우기.
"""



"""
set c++ set과 유사.
중복 불가, 순서 없음
"""

s1 = set()
s2 = set([1,2,3])
s3 = set(("hello"))

print(s1)
print(s2)
print(s3)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)  #합집합
print(s1 | s2)  #교집합
print(s1 - s2)  #차집합

#값 추가, 삭제
s3 = set(("hello"))
#하나 추가
s3.add('p')
print(s3)
#다수 추가
s3.update('opqw')
print(s3)
#삭제
s3.remove('l')