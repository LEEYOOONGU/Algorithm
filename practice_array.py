import time
start_time = time.time()

array = [3,5,1,2,4]
summary = 0

for i in array:
    for j in array:
        temp = i*j
        print(temp)

end_time = time.time()
print("time :", end_time - start_time)

