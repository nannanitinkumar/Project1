
N = input()
dataT = raw_input().split()

for i in range(0,len(dataT)):
    dataT[i] = int(dataT[i])

T = tuple(dataT)

print hash(T)
