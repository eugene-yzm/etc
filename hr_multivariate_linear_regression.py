## FOLLOWING IS A EXAMPLE OF BEHAVIOR
## THE SCRIPT READS INPUT FILE OF A SET OF FEATURES AND ASSOCIATED RESULTS
## THEN THE SCRIPT PRINTS PREDICTIONS BASED ON TEST PARAMETERS
## https://www.hackerrank.com/challenges/predicting-house-prices

## Sample Input

# 2 7
# 0.18 0.89 109.85
# 1.0 0.26 155.72
# 0.92 0.11 137.66
# 0.07 0.37 76.17
# 0.85 0.16 139.75
# 0.99 0.41 162.6
# 0.87 0.47 151.77
# 4
# 0.49 0.18
# 0.57 0.83
# 0.56 0.64
# 0.76 0.18

## Sample Output

# 105.22
# 142.68
# 132.94
# 129.71


import fileinput
from sklearn import linear_model

features = 0
examples = 0
f = []
e = []
clf = linear_model.LinearRegression()

for line in fileinput.input():
    if fileinput.lineno() == 1:
        features = int(line.split()[0])
        examples = int(line.split()[1])
        f = [[0]*features for i in range(0,examples)]
        e = [0]*examples
    else:
        if fileinput.lineno() < examples + 2:
            item = line.strip().split()
            for i in range(0,features):
                f[fileinput.lineno() - 2][i] = float(item[i])
            e[fileinput.lineno()-2] = float(item[features])
        elif fileinput.lineno() == examples + 2:
            clf.fit(f,e)
        elif fileinput.lineno() > examples + 2:
            item = line.strip().split()
            coordinate = []
            for i in item:
                coordinate.append(float(i))
            print clf.predict(coordinate)[0]
