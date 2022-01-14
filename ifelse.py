import time
start_time = time.time()

x = 15
if x >= 10:
    print(x)


score = 85

if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")

end_time = time.time()
print("time :", end_time - start_time)


