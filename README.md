# data-complexity
The Data Complexity Measures in Python


## Install
```bash
$ pip install data-complexity
```


## How it works
### Maximum Fisher's Discriminant Ratio (F1)
```python
from dcm import dcm
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

index, F1 = dcm.F1(X, y)
```

### Other Measures
Coming soon...


## References
[1] How Complex is your classification problem? A survey on measuring classification complexity, https://arxiv.org/abs/1808.03591

[2] The Extended Complexity Library (ECoL), https://github.com/lpfgarcia/ECoL
