# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput


def makegrid():
    grid = {}
    for i in range(1,100):
        grid[i] = []
        for j in range(1,7):
            if (i + j) <= 100:
                grid[i].append(i + j)
            else:
                pass
    return grid    

play = [False, False]
grid = makegrid()
for line in fileinput.input():
    if fileinput.isfirstline() is not True:        
        #ladders
        if fileinput.lineno() % 3 == 0: 
            ld = list(line.strip().split())
            for it in ld:
                pair = map(int, it.split(','))
                grid[pair[0]]=[pair[1]]
            play[0] = True
            
        #snakes
        elif fileinput.lineno() % 3 == 1:
            sn = list(line.strip().split())
            for it in ld:
                pair = map(int, it.split(','))
                grid[pair[0]]=[pair[1]]
            play[1] = True
            
        if play == [True, True]:
            paths = {}
            for i in range(1,100):
                for path in grid[i]:
                    if i == 1:
                        paths[path] = 0
                    else:
                        if path in paths:
                            if paths[path] > paths[i] + 1:
                                paths[path] = paths[i] + 1
                        else:
                            paths[path] = paths[i] + 1
            print paths[100]        
            grid = makegrid()
            play = [False, False]