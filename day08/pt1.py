file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day08/input.txt", "r")
sequence = file.readline()
lines = file.read().split('\n')
nodes = []
next_nodes = []
for line in lines:
    node, next_node = (line.split(' = '))
    nodes.append(node)
    next_nodes.append(next_node.strip('()').split(', '))

def nextNode(next_node, command):
    if(command=='L'):
        return next_node[0]
    elif(command=='R'):
        return next_node[1]
    return 

index, index2, counter = nodes.index('AAA'), 0, 0
while nodes[index]!='ZZZ':
    index = nodes.index(nextNode(next_nodes[index],sequence[index2]))
    counter += 1
    index2 += 1
    if(index2==len(sequence)-1):
        index2=0

print(counter)

file.close()