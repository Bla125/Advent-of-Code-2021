from zoautil_py import datasets


input_data = datasets.read('Z00620.ADVINPUT(DAY1IN)')

input_num = list(input_data.split())

largercount = 0
j = 0
for i in range(0,len(input_num)):
    j = i - 1
    if int(input_num[i]) > int(input_num[j]):
        largercount += 1

print(largercount)

with open(r'/z/z00620/advpython/output','w') as file:
    file.write(str(largercount))