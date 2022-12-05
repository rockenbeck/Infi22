# Sorry for the mishmash of Dutch and English; I can only sort of read Dutch!

def KPS(file):
    x,y = 0,0 # current position
    dir = 0 # "North", though how he can face north while starting at the North Pole is perplexing...
    dx,dy = 0,1 # current direction as step deltas
    sporen = set() # set of all footprint locations

    for line in open(file).readlines():
        command,arg = line.split(' ')
        if command == "draai":
            # turn and remember step deltas
            dir += int(arg)
            assert(dir % 45 == 0) # seems implied by instructions: else where to step to?
            dx,dy = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1, 0), (-1, 1)][(dir // 45) % 8]
        elif command == "loop":
            s = int(arg)
            # leave a footprint at each location
            for i in range(0,s):
                x += dx
                y += dy
                sporen.add((x,y))
        elif command == "spring":
            s = int(arg) * 1
            x += dx * s
            y += dy * s
            # leave a footprint at the end of the jump
            sporen.add((x,y))
        else:
            # unknown command
            assert(False)

    print(x,y,abs(x) + abs(y)) # part A

    # part B: Draw the map as ASCII art
    xmin,ymin = min(sporen)
    xmax,ymax = max(sporen)
    for y in range(ymax, ymin - 1, -1):
        print(''.join(['*' if (x,y) in sporen else ' ' for x in range(xmin, xmax + 1)]))

KPS("test.txt")
KPS("lijst.txt")
