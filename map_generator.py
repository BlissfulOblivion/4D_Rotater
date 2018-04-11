# Holds the function that generates maps from grids and instructions

def genmap(puzzle):
    rawmaps = [line.strip() for line in open(puzzle) if "." not in line]
    maps = [[['x' for col in range(12)] for row in range(12)] for plane in range(4)]
    for plane in range(len(maps)):
        for row in range(len(maps[plane])):
            for col in range(len(maps[plane][row])):
                if rawmaps[0][0] == 'X':
                    maps[plane][row][col] = 1
                else:
                    maps[plane][row][col] = 8
                rawmaps[0] = rawmaps[0][1:]
            del(rawmaps[0])
    return maps
