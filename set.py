import time
start_time = time.time()


data = set([1,1,2,3,4,4,4,4,4,5])
print(data)
data = {1,2,3,4,5,6,6,6,6,6,6,6,6}
print(data)

a = set([1,2,3,4,5])
b = set([3,4,5,6,7,8])

#합집합
print(a | b)
#교집합
print(a & b)
#차집합
print(a - b)

data = set([1,2,3])
print(data)

data.add(4)
print(data)

data.update([5,6])
print(data)

data.remove(3)
print(data)


end_time = time.time()
print("time :", end_time - start_time)


