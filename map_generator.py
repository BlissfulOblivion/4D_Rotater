# Holds the function that generates maps from grids and instructions

def genmap(mapfeats,mapedits):
    fullmap = [[0 for a in b] for b in mapfeats]
    for i in range(len(mapfeats)):
        for j in range(len(mapfeats[i])):
            fullmap[i][j] = mapfeats[i][j]
    for edit in mapedits:
        y,x,tile = edit
        for row in range(y[0],y[1]):
            for col in range(x[0],x[1]):
                fullmap[row][col] = tile
    return fullmap


