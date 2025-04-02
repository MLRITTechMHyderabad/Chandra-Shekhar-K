M=int(input("rows: "))
N=int(input("Cols: "))
matrix=[[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]]
res=[[0 for x in range(M)] for y in range(N)]
for i in range(N):
    for j in range(M):
        res[i][j]=matrix[j][i]

print("transpose of a given matrix: ")

for i in range(N):
    for j in range(M):
        print(res[i][j]," ",end=' ')
    print()