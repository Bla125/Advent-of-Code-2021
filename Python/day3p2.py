from zoautil_py import datasets

input = datasets.read('Z00620.ADVINPUT(DAY3IN)')
line = list(input.split('\n'))

line = list(map(str.strip, line))

def find_rating(oxy_scrub):
    global line
    oxy_line = line[:]
    scrub_line = line[:]
    oxygen = ''
    scrubber = ''
    ones = []
    zeros = []
    if oxy_scrub == 'oxygen':
        for col in range(0,len(oxy_line[0])):
            if len(oxy_line) == 1: break
            for row in range(0,len(oxy_line)):
                if int(oxy_line[row][col]) == 1:
                    ones.append(oxy_line[row])
                else:
                    zeros.append(oxy_line[row])

            if len(ones) >= len(zeros):
                oxy_line = ones[:]
                ones = []
                zeros = []
            else:
                oxy_line = zeros[:]
                ones = []
                zeros = []                
        oxygen = ''.join(map(str, oxy_line[0]))
        return int(oxygen, 2)


    elif oxy_scrub == 'scrubber':
        for col in range(0,len(scrub_line[0])):
            if len(scrub_line) == 1: break
            for row in range(0,len(scrub_line)):
                if int(scrub_line[row][col]) == 1:
                    ones.append(scrub_line[row])
                else:
                    zeros.append(scrub_line[row])

            if len(zeros) <= len(ones):
                scrub_line = zeros[:]
                ones = []
                zeros = []
            else:
                scrub_line = ones[:]
                ones = []
                zeros = []
        scrubber = ''.join(map(str, scrub_line[0]))
        return int(scrubber, 2)


oxygen = find_rating('oxygen')
scrubber = find_rating('scrubber')

power = oxygen * scrubber

datasets.write('Z00620.ADVPY(OUTPUT)', content=str(power), append=False)