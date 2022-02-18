from zoautil_py import datasets

input = datasets.read('Z00620.ADVINPUT(DAY2IN)')
line = list(input.split('\n'))

horizontal = 0
depth = 0
total = 0

for i in range(0,len(line)):
    phrase = str(line[i].split(' ')[0])
    num = int(line[i].split(' ')[1])   
    if phrase in 'forward':
        horizontal += num
    elif phrase in 'down':
        depth += num
    elif phrase in 'up':
        depth -= num

total = horizontal * depth

with open(r'/z/z00620/advpython/output','w') as file:
    file.write(str(total))