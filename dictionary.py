import time
start_time = time.time()

data = dict()
data['사과'] = "Apple"
data['바나나'] = "Banana"
data['코코넛'] = "Coconut"

print(data)

if '사과' in data:
    print('사과를 키로 가지는 데이터가 존재합니다')

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])

end_time = time.time()
print("time :", end_time - start_time)


