# importing relevant modules
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# creating grid
grid = Grid(matrix = matrix)

# start and end point
start = grid.node(0,0)
end = grid.node(9,9)

# finder
finder = AStarFinder(diagonal_movement = DiagonalMovement.always)

# using the finder to find the path
path,runs = finder.find_path(start,end,grid)

# print results
print(path)
print(runs) # tells us how many times it ran through the matrix to find the shortest path
