import sys, copy

Y, X = map(int,sys.stdin.readline().split())
Z = []
answer = []
pip = 0
for i in range(Y):
    Z.append(list(input()))
def calPipeLine(y, pipLen, z):
    global pip, Z
    if pipLen == 4:
        pip += 1
        Z = copy.deepcopy(z)
        return True
    if y - 1 >= 0 and z[y - 1][pipLen+1:pipLen + 2] != ['x']:
        temp = copy.deepcopy(z)
        temp[y - 1][pipLen+1:pipLen + 2] = 'x'
        if pipLen == 0:
            temp[y][0] = 'x'
        calPipeLine(y - 1, pipLen + 1, temp)
    elif not z[y][pipLen+1:pipLen + 2] == ['x']:
        temp = copy.deepcopy(z)
        temp[y][pipLen+1:pipLen + 2] = 'x'
        if pipLen == 0:
            temp[y][0] = 'x'
        calPipeLine(y, pipLen + 1, temp)
    elif y + 1 <= Y - 1 and z[y + 1][pipLen+1:pipLen + 2] != ['x']:
        temp = copy.deepcopy(z)
        temp[y + 1][pipLen+1:pipLen + 2] = 'x'
        if pipLen == 0:
            temp[y][0] = 'x'
        calPipeLine(y + 1, pipLen + 1, temp)
    return False
for i in range(Y):
    calPipeLine(i,0,Z)
print(pip)