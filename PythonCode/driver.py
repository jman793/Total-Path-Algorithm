#this file will be the driver program used for all three of the algorithms proposed
from Algorithms import basic_recursion

N=10
#This will define a grid of size NxN
#The grid will be defined as follows 1 a valid square, 0 an invalid square, 2 the final square
#For now the input will be non-random
Grid=[[1 for i in range(N)]for c in range(N)]
Grid[N-1][N-1]=2
Grid[N-5][N-2]=0
Grid[N-7][N-4]=0
Grid[N-1][N-1]=0
Grid[N-9][N-8]=0
Grid[0][N-2]=0
Grid[N-5][N-6]=0
Grid[N-4][N-9]=0
Grid[N-3][N-4]=0
#This function will print out the grid in a neat fashion
def print_grid(G):
    for i in range(len(G)):
        print G[i]

print_grid(Grid)
print basic_recursion(Grid,0,0)
