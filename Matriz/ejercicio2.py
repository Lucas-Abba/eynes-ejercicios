from random import randint


def randomMatrix():
    random_matrix_array = [[randint(1,4) for j in range(5)] for i in range(5)]
    return random_matrix_array

def findSequence(m):
    # CHECKS ROWS
    for i in range(len(m)):
        if (m[i][0]+1 == m[i][1] and m[i][1]+1 == m[i][2] and m[i][2]+1 == m[i][3]):
            return('Posicion inicial: m[%d][0]  Posicion Final m[%d][3]' % (i,i))
        if (m[i][1]+1 == m[i][2] and m[i][2]+1 == m[i][3] and m[i][3]+1 == m[i][4]):  
            return('Posicion inicial: m[%d][1]  Posicion Final m[%d][4]' % (i,i))
    # CHECKS COLUMNS
    for i in range(len(m)):
        if (m[0][i]+1 == m[1][i] and m[1][i]+1 == m[2][i] and m[2][i]+1 == m[3][i]):
            return('Posicion inicial: m[0][%d]  Posicion Final m[3][%d]' % (i,i))
        if (m[1][i]+1 == m[2][i] and m[2][i]+1 == m[3][i] and m[3][i]+1 == m[4][i]):  
            return('Posicion inicial: m[1][%d]  Posicion Final m[4][%d]' % (i,i))


m = randomMatrix()
for a in m:
    print(a)

print(findSequence(m))

