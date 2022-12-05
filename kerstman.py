# Sorry for the mishmash of Dutch and English; I can only sort of read Dutch!

def KPS(file):
    x,y = 0,0
    dir = 0
    sporen = set()

    for line in open(file).readlines():
        if line[:5] == "draai":
            dir += int(line[6:])
            dx,dy = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1, 0), (-1, 1)][(dir // 45) % 8]
        elif line[:4] == "loop":
            s = int(line[5:])
            for i in range(0,s):
                x += dx
                y += dy
                sporen.add((x,y))
        elif line[:6] == "spring":
            s = int(line[7:]) * 1
            x += dx * s
            y += dy * s
            sporen.add((x,y))
        else:
            assert(False)

    print(x,y,abs(x) + abs(y))

    xmin = min([x for x,y in sporen])
    xmax = max([x for x,y in sporen]) + 1
    ymin = min([y for x,y in sporen])
    ymax = max([y for x,y in sporen]) + 1

    for y in range(ymax - 1, ymin - 1, -1):
        print(''.join(['*' if (x,y) in sporen else ' ' for x in range(xmin, xmax)]))

# KPS("test.txt")
KPS("lijst.txt")
