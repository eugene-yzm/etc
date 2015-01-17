# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

inputs = []
s = set()
for line in fileinput.input():
    if fileinput.isfirstline() is not True:
        l = map(int,(line.strip().split(" ")))
        for x in l: s.add(x)
        inputs.append(l)
print inputs

u = set()
l = []
for x,y in enumerate(s):
    slot = s
    slot.difference(u)
    
    for group in inputs:
        slot = slot.difference(set(group[x:]))
    print slot
    possible = []
    for i in slot: possible.append(i)
    u.add(max(possible))
    print slot
    
for x in l:
    print x,
        
    
    