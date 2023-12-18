file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day09/input.txt", "r")
history = file.readline().split()

def diff_list(history):
    aux=[]
    for i in range(1, len(history)):
        aux.append(int(history[i])-int(history[i-1]))
    return aux

def ext_values(history):
    ans=0
    last_values=[int(history[-1])]
    aux=diff_list(history)
    while aux != [0 for i in range(len(aux))]:
        last_values.append(aux[-1])
        aux=diff_list(aux)
    ans = sum(last_values)
    return ans

soma = 0
while history:
    aux = ext_values(history)
    soma = soma + aux
    history = file.readline().split()

print(soma)

file.close()