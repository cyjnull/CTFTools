def indexes(x, y, n):
    return x * n + y


def isin(x, y, n):
    if x < 0 or x >= n:
        return 0
    if y < 0 or y >= n:
        return 0
    return 1


def seek2(x, y, n, maze, accessible):
    accessible[indexes(x, y, n)] = 'O'
    for num in range(n):
        for cd_x in range(0, n):
            for cd_y in range(0, n):
                if accessible[indexes(cd_x, cd_y, n)] == 'O':
                    if isin(cd_x + 1, cd_y, n):
                        if maze[indexes(cd_x + 1, cd_y, n)] == 'O':
                            accessible[indexes(cd_x + 1, cd_y, n)] = 'O'
                    if isin(cd_x - 1, cd_y, n):
                        if maze[indexes(cd_x - 1, cd_y, n)] == 'O':
                            accessible[indexes(cd_x - 1, cd_y, n)] = 'O'
                    if isin(cd_x, cd_y + 1, n):
                        if maze[indexes(cd_x, cd_y + 1, n)] == 'O':
                            accessible[indexes(cd_x, cd_y + 1, n)] = 'O'
                    if isin(cd_x, cd_y - 1, n):
                        if maze[indexes(cd_x, cd_y - 1, n)] == 'O':
                            accessible[indexes(cd_x, cd_y - 1, n)] = 'O'


filename = 'in.txt'
filename = filename.decode('utf-8')
fi = open(filename)
ctf = ''
T = int(fi.readline())
for i in range(T):
    print('T= ', i)
    n = int(fi.readline())
    incd = fi.readline().split(' ')
    outcd = fi.readline().split(' ')
    for j in range(2):
        incd[j] = int(incd[j]) - 1
        outcd[j] = int(outcd[j]) - 1
    maze = []
    accessible = []
    line = ''
    for x in range(n):
        line = fi.readline()
        for y in range(n):
            maze.append(line[y])
            accessible.append('X')
    seek2(incd[0], incd[1], n, maze, accessible)
    if accessible[indexes(outcd[0], outcd[1], n)] == 'O':
        ctf += '1'
    else:
        ctf += '0'
flag = ''
for i in range(0, len(ctf), 8):
    flag += chr(int(ctf[i:i + 8], 2))
print(flag)
print(flag.decode('base64'))