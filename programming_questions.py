import collections

# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def checkConnected(C,x):
    l = []
    for i,e in enumerate(C):
        if i == x:
            l.append(e)
        elif e == x:
            l.append(i)
        else:
            pass
    return l

# def recurse(C,K,D,R,x,d,p):
#     d += 1
#     l = []
#     if d <= K:
#         conn = checkConnected(C,x)
#         if len(conn) > 0:
#             if x in conn:
#                 conn.remove(x)
#                 for n in conn:
#                     if D[n] < R[d-1]:
#                         pass
#                     else:
#                         p.append(n)
#                         p = recurse(C,K,D,R,n,d,p)
#                         return p
#     else:
#         return p

        
def solution(K, C, D):
    # write your code in Python 2.7
    # K = num of cities to visit
    # C = connected
    # D = attractiveness  
    max_i = []
    max_v = max(D)
    rev_l = sorted(D, reverse=True)   
    
    for i, e in enumerate(D):
        if max_v == e:
            max_i.append(i)   
                        
    paths = []
    for i in max_i:
        p = collections.deque()
        p.append(i)
        r_slots = K 
        valid_moves = checkConnected(C,i)
        valid_val = rev_l[1:1+len(valid_moves)]
        o_m = []
        for move in valid_moves:
            o_m.append([move, D[move]])
        o_m = sorted(o_m,key=lambda l:l[1], reverse=True)
        print o_m
        
        for j in valid_moves:
            if D[j] in valid_val:
                valid_moves.remove(j)
                valid_val.remove(D[j])
                r_slots -= 1
                print valid_moves
        print valid_val
