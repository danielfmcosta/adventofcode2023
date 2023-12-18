import math

file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day08/input.txt", "r")
sequence = file.readline()
lines = file.read().split('\n')
nodes = []
next_nodes = []
for line in lines:
    node, next_node = (line.split(' = '))
    nodes.append(node)
    next_nodes.append(next_node.strip('()').split(', '))

indexes = []
for i in range(len(nodes)):
    if(nodes[i].endswith('A')):
        indexes.append(nodes.index(nodes[i]))

def nextNode(next_node, command):
    if(command=='L'):
        return next_node[0]
    elif(command=='R'):
        return next_node[1]
    return 

flags = [True for i in range(len(indexes))]
indexS, counterS = 0, 0
counters = [0 for i in range(len(indexes))]
while flags[0]:
    indexes[0] = nodes.index(nextNode(next_nodes[indexes[0]],sequence[indexS]))
    counterS += 1
    indexS += 1
    if(indexS==len(sequence)-1):
        indexS=0
    if(nodes[indexes[0]].endswith('Z')):
        counters[0]=counterS
        flags[0]=False
indexS, counterS = 0, 0
while flags[1]:
    indexes[1] = nodes.index(nextNode(next_nodes[indexes[1]],sequence[indexS]))
    counterS += 1
    indexS += 1
    if(indexS==len(sequence)-1):
        indexS=0
    if(nodes[indexes[1]].endswith('Z')):
        counters[1]=counterS
        flags[1]=False
indexS, counterS = 0, 0
while flags[2]:
    indexes[2] = nodes.index(nextNode(next_nodes[indexes[2]],sequence[indexS]))
    counterS += 1
    indexS += 1
    if(indexS==len(sequence)-1):
        indexS=0
    if(nodes[indexes[2]].endswith('Z')):
        counters[2]=counterS
        flags[2]=False
indexS, counterS = 0, 0    
while flags[3]:
    indexes[3] = nodes.index(nextNode(next_nodes[indexes[3]],sequence[indexS]))
    counterS += 1
    indexS += 1
    if(indexS==len(sequence)-1):
        indexS=0
    if(nodes[indexes[3]].endswith('Z')):
        counters[3]=counterS
        flags[3]=False
indexS, counterS = 0, 0
while flags[4]:
    indexes[4] = nodes.index(nextNode(next_nodes[indexes[4]],sequence[indexS]))
    counterS += 1
    indexS += 1
    if(indexS==len(sequence)-1):
        indexS=0
    if(nodes[indexes[4]].endswith('Z')):
        counters[4]=counterS
        flags[4]=False
indexS, counterS = 0, 0
while flags[5]:
    indexes[5] = nodes.index(nextNode(next_nodes[indexes[5]],sequence[indexS]))
    counterS += 1
    indexS += 1
    if(indexS==len(sequence)-1):
        indexS=0
    if(nodes[indexes[5]].endswith('Z')):
        counters[5]=counterS
        flags[5]=False

z1 = int((counters[0]*counters[1])/math.gcd(counters[0],counters[1]))
z2 = int((z1*counters[2])/math.gcd(z1,counters[2]))
z3 = int((z2*counters[3])/math.gcd(z2,counters[3]))
z4 = int((z3*counters[4])/math.gcd(z3,counters[4]))
z5 = int((z4*counters[5])/math.gcd(z4,counters[5]))
print(z5)

print(counters)

file.close()