from zoautil_py import datasets


input_data = datasets.read('Z00620.ADVINPUT(DAY1IN)')

input_num = list(input_data.split())

largercount = 0
for i in range(0,len(input_num)):
# i + 3 is the sliding window, break if it is outside range
    if i + 3 > len(input_num) - 1:
        break
    a1 = int(input_num[i])
    a2 = int(input_num[i+1])
    a3 = int(input_num[i+2])
    b1 = int(input_num[i+1])
    b2 = int(input_num[i+2])
    b3 = int(input_num[i+3])
    total_a = a1 + a2 + a3
    total_b = b1 + b2 + b3
    if total_b > total_a:
        largercount += 1

print(largercount)

with open(r'/z/z00620/advpython/output','w') as file:
    file.write(str(largercount))


