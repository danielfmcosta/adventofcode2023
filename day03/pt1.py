symb = ['=', '*', '-', '@', '$', '+', '#', '&', '%', '/']

def rem_num_arount_symb (matrix, i, j):
    #matrix[i][0][j] = '.'
    aux_list = list(matrix[i][0])
    aux_list[j] = '.'
    matrix[i][0] = ''.join(aux_list)
    if(j > 0 and matrix[i][0][j-1].isdigit()):
        rem_num_arount_symb(matrix, i, j-1)
    if(j < len(matrix[i][0]) - 1 and matrix[i][0][j+1].isdigit()):
        rem_num_arount_symb(matrix, i, j+1)

def check_char (matrix, i, j): # i and k are rows, j and h are columns
    for k in range(i-1, i+2):
        for h in range(j-1, j+2):
            if(matrix[k][0][h].isdigit()):
                rem_num_arount_symb(matrix, k, h)             

file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventcode23/day03/input.txt", "r")
content = file.readline().strip('\n')
matrix1, matrix2 = [], []
num_not_part = 0
num_tot = 0
while content:
    matrix1.append([content])
    matrix2.append([content])
    content = file.readline().strip('\n')


for i in range(1, len(matrix1)):
    for j in range(1, len(matrix1[i][0])):
        if (matrix1[i][0][j] in symb):
            check_char(matrix1, i, j)

for i in range(len(matrix1)): #sum of numbers not a part
    aux = matrix1[i][0].split('.')
    print(aux)
    for j in range(len(aux)):
        if(aux[j].isdigit()):
            num_not_part += int(aux[j])

for i in range(len(matrix2)): #sum of all numbers
    for char in "=*-@$+#&%/":
        matrix2[i][0]=matrix2[i][0].replace(char, ".")
    aux = matrix2[i][0].split('.')
    print(aux)
    for j in range(len(aux)):
        if(aux[j].isdigit()):
            num_tot += int(aux[j])

print('\n'.join([el[0] for el in matrix1]))
print(num_tot-num_not_part)
file.close()