import numpy as np
import sklearn
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree


if __name__ == "__main__":
    p = pd.read_csv("data4.csv")
    p = np.array(p)
    X = p[:,1:11]
    y = p[:,11]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, y)
    tree.plot_tree(clf)
    plt.show()


