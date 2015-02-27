#read input from STDIN. Print output to STDOUT
N,l = map(int,raw_input().split())

nodes = []
connections = []
def ck_conn(n1, n2):
    found = False
    for cn in connections:
        if len(connections)>0:
            terms = set()
            for tm in cn:
                if n1 == tm or n2 == tm:
                    found = True
                    terms.add(n1)
                    terms.add(n2)
    if found is False:
        mk_conn(n1,n2)

def mk_conn(n1, n2):
    connections.append(set([n1,n2]))

def combinations():
    sum = 0
    for i, o in enumerate(connections):
        itm = 0
        for j in range(i+1,len(connections)):
            itm += len(connections[i])*len(connections[j])
        sum += itm
    print sum
for i in xrange(l):
    a,b = map(int,raw_input().split())
    ck_conn(a,b)
    # Store a and b in an appropriate data structure
combinations()
# Compute the final result using the inputs from above


