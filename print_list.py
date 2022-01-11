import time
start_time = time.time()

a = [1,2,3,4,5,6,7,8,9]
print(a)
print(a[4])

a = list()
print(a)

n = 10
a = [0]*n
for i in range(10):
    a[i] = a[i]+i

print(a[-1])
print(a[-3])
print(a[1:4])

#0~19까지의 짝수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 0]
print(array)

#9까지의 제곱수를 저장하는 리스트
array = [i*i for i in range(1,10)]
print(array)

#n*m 2차원 리스트 배열 초기화 
n = 3
m = 4  
array = [[0]*m for _ in range(n)]
print(array)
array[1][1] = 1
array[0][1] = 1
print(array)

# ===============================================================================

a = [1,4,3]
print("기본 리스트: ", a)

a.append(2)
print("삽입: ", a)

a.sort()
print("오름차순 정렬: ", a)

a.sort(reverse= True)
print("내림차순 정렬: ", a)

a.reverse()
print("원소 뒤집기: ", a)

a.insert(2,3)
print("인덱스 2에 3 추가: ", a)

print("데이터가 3인 갯수", a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제: ", a)



#특정 세트가 리스트에 포함되지 않았을 경우에만 프린트 
a = [1,2,3,4,5,5,5]
remove_set = [3,5]

result = [i for i in a if i not in remove_set]
print(result)

end_time = time.time()
print("time :", end_time - start_time)


