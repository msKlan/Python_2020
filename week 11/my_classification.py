from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()

print(type(iris))
print(iris.keys())
X = iris.data  # features
y = iris.target  # result or classification
