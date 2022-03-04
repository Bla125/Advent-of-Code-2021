from zoautil_py import datasets

input = datasets.read('Z00620.ADVINPUT(DAY3IN)')
line = list(input.split('\n'))

line = list(map(str.strip, line))
ones = [0 for i in range(len(line[0]))]
zeros = [0 for i in range(len(line[0]))]

for row in range(0,len(line)):
    for col in range(0,len(line[row])):
        if int(line[row][col]) == 1:
            ones[col] += 1
        else:
            zeros[col] += 1

gamma_bin = [0 for i in range(len(ones))]
epsilon_bin = [0 for i in range(len(ones))]

for col in range(0,len(ones)):
    if ones[col] > zeros[col]:
        gamma_bin[col] = 1
        epsilon_bin[col] = 0
    else:
        gamma_bin[col] = 0
        epsilon_bin[col] = 1


def bin_to_dec(bin_num):
    dec_num = ''.join(map(str, bin_num))
    return int(dec_num,2)

gamma_dec = bin_to_dec(gamma_bin)
epsilon_dec = bin_to_dec(epsilon_bin)

power = gamma_dec * epsilon_dec
datasets.write('Z00620.ADVPY(OUTPUT)', content=str(power),append=False)
