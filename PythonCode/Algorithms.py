#This will be where the algorithms used are programmed

#This first algorithm is a basic recursive method to solve the problem
def basic_recursion(G,i,j):
    N=len(G)
    if i==N-1 and j==N-1:
        return 0
    elif j==N-1 and G[i+1][j]!=0:
        return 1
    elif j==N-1 and G[i+1][j]==0:
        return 0
    elif i==N-1 and G[i][j+1]!=0:
        return 1
    elif i==N-1 and G[i][j+1]==0:
        return 0
    elif G[i+1][j]==0 and G[i][j+1]==0:
        return 0
    else:
        return basic_recursion(G,i+1,j)+basic_recursion(G,i,j+1)
    
 def memoized(i,j,V,ctr):
    if V[i][j]!=q:
        return V[i][j]
    if i==n-1 and j==n-1 and V[i][j]!=q:
        V[i][j]=V[i-1][j]+V[i][j-1]
        return V[i][j]
    if i==n-1 and V[i][j]!=q:
        V[i][j]=V[i-1][j]+1
        return V[i][j]
    elif i==n-1:
        V[i][j]=1
        return V[i][j]
    if j==n-1 and V[i][j]!=q:
        V[i][j]=V[i][j-1]+1
        return V[i][j]
    elif j==n-1:
        V[i][j]=1
        return V[i][j]
    else:
        V[i][j]=memoized(i+1,j,V,ctr)+memoized(i,j+1,V,ctr)
        return V[i][j]
