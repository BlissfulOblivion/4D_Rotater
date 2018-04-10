### Contains all the puzzles written for this game in grid form
from map_generator import genmap

## TILES KEY
# 0 - blank
# 1 - grass
# 2 - waterground
# 3 - water
# 4 - fireground
# 5 - lava
# 6 - cloud
# 7 - sky
# 8 - pit

##############################
# LEVEL 1
##############################
map1 = [[1 for col in range(12)] for row in range(12)]

map1feats = []

maps = [map1]
mapfeats = [map1feats]
puzzle1 = [genmap(mapx,mapxfeats) for mapx,mapxfeats in zip(maps,mapfeats)]

##############################
# LEVEL 2
##############################
map1 = [[1 for col in range(12)] for row in range(12)]

map1feats = []

maps = [map1]
mapfeats = [map1feats]
puzzle2 = [genmap(mapx,mapxfeats) for mapx,mapxfeats in zip(maps,mapfeats)]

##############################
# LEVEL 3
##############################
map1 = [[8 for col in range(12)] for row in range(12)]
map2 = [[3 for col in range(12)] for row in range(12)]

map1feats = [[(0,3),(0,12),1],[(9,12),(0,12),1]]
map2feats = [[(0,12),(6,9),2]]

maps = [map1,map2]
mapfeats = [map1feats,map2feats]
puzzle3 = [genmap(mapx,mapxfeats) for mapx,mapxfeats in zip(maps,mapfeats)]

##############################
# LEVEL 4
##############################
map1 = [[8 for col in range(12)] for row in range(12)]
map2 = [[3 for col in range(12)] for row in range(12)]
map3 = [[5 for col in range(12)] for row in range(12)]
map4 = [[7 for col in range(12)] for row in range(12)]

map1feats = [[(0,3),(0,12),1],[(9,12),(0,12),1]]
map2feats = [[(0,6),(6,9),2],[(3,6),(3,6),2],[(9,12),(0,3),2]]
map3feats = [[(3,9),(3,6),4],[(6,9),(6,9),4],[(9,12),(0,3),4]]
map4feats = [[(6,9),(6,9),6],[(9,12),(0,12),6]]

maps = [map1,map2,map3,map4]
mapfeats = [map1feats,map2feats,map3feats,map4feats]
puzzle4 = [genmap(mapx,mapxfeats) for mapx,mapxfeats in zip(maps,mapfeats)]

##############################
# LEVEL 5
##############################




##############################
# LEVEL 6
##############################'''






























