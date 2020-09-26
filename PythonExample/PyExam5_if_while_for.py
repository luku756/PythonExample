"""
if
"""
print("\nif!!\n")
#기본 문법
flag = 5

if flag == 5:
    print("5")
else :
    print("noe")

flag -= 1

if flag == 5:
    print("5")
else :
    print("noe")

    
if flag == 5:
    print("5")
elif flag == 4:
    pass#아무것도 하지 않음. 빈 if문
else :
    print("noe")

print("---")

#리스트(튜플, 문자열) 조건
lists = [1,2,3]

if 1 in lists :
    print("yes 1")
else:
    print("no 1")
    
if 4 in lists :
    print("yes 4")
else:
    print("no 4")


"""
while
"""
print("\nwhile!!\n")
cnt = 5
while cnt >= 0 :
    print(cnt)
    cnt -= 1;
    if cnt==2:
       break

   
"""
for
"""
print("\nfor!!\n")

lists = ["one", "two", "three"]
for i in lists:
    print(i)
    
print("")

    
lists = ["one", "two", "three"]
for i in lists:
    if i == "two" :
       continue;
    print(i)

    #정형화 된 경우에만 사용가능. 중간이 (3,4,5)이러면 에러.
a = [(1,2), (3,4) ,(5,6)]
for (i,j) in a:
    print("i : {0}, j : {1}".format(i,j))
  
"""
range 사용법
"""
a= range(10) # 0~9
print(a) 

a= range(1,11) # 1~10
print(a) 

add=0
for i in range(1,11) :
    add = add + i
print(add)


print("")

"""
일반적으로 C에서 쓰이는 for(i=0;i<n;i++) 구현법
"""
# i=min ; i< max; i++
min = 3
max = 10
for i in range(min, max) :
    print("a is {0}".format(i))

#배열 접근법, index 포함
lists = [12,4352,3,24,2,456,1]
for i in range(len(lists)):
    print("lists {0} is {1}".format(i,lists[i]))
    
#배열 접근법, index 포함
lists = [12,4352,3,24,2,456,1]
for i, val in enumerate(lists):
    print("lists {0} is {1}".format(i,val))


#리스트 내포
a = [1,2,3,4]
result = [num* 3 for num in a] #리스트 안의 모든 변수에 적용
print(result)

result = [num* 3 for num in a if num%2 == 0] #리스트 안의 모든 변수 중 짝수에 적용
print(result)

#구구단 계산
##for간은 엔터로도 구분 가능
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)