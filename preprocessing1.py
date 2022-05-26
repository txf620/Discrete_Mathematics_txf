import copy
import pandas as pd
import numpy as np
import random

if __name__ == "__main__":
    p = pd.read_csv('data.csv')
    dic = [dict(),dict(),dict(),dict(),dict(),dict(),dict()]
    dic2 = [dict(),dict(),dict(),dict(),dict(),dict(),dict()]
    p = np.array(p)
    p = p[0:17,1:8]
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] not in dic[j]:
                dic[j][p[i][j]] = len(dic[j])
                dic2[j][len(dic[j]) - 1] = p[i][j]

    pp = np.zeros((17,7))
    for i in range(len(p)):
        for j in range(len(p[i])):
            p[i][j] = dic[j][p[i][j]]
            print(dic2[j][p[i][j]],end = ' ')
        print()

    t = []
    for i in range(len(p)):
        temp = list(p[i])
        for j in range(4):
            temp.append(random.randint(0,1))
        t.append(copy.deepcopy(temp))

    p = np.array(t)

    print(p)
    p = pd.DataFrame(p)
    p.to_csv("data2.csv")
    print(p)

