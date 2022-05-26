import copy
import pandas as pd
import numpy as np
import random

if __name__ == "__main__":
    p = pd.read_csv('data3.csv')

    p = np.array(p)
    p1 = p[0:17,1:12]

    for i in range(5):
        p1 = np.insert(p1, 0, values = p1, axis = 0)

    for i in range(300):
        i1 = random.randint(0,len(p1) - 1)
        i2 = random.randint(0,len(p1) - 1)
        p1[[i1,i2],:] = p1[[i2,i1],:]

    p1 = pd.DataFrame(p1)
    p1.to_csv("data4.csv")
    print(p1)


