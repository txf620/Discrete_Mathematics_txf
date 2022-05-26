import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA, FactorAnalysis

pca = PCA(n_components = 4)

p = pd.read_csv("data4.csv")
p = np.array(p)
X = p[:, 1:11]
y = p[:, 11]

pca.fit(X,y)
xx = pca.transform(X)

xx = np.insert(xx, 4, values = y, axis=1)

p1 = pd.DataFrame(xx)
p1.to_csv("data_pca.csv")
print(p1)
