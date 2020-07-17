import pandas as pd
from dcm import dcm
import datasets

dataset_file = 'examples/datasets/creditcard.csv'
datasets.download_creditcard(dataset_file)

print("Loading dataset ... ", end="", flush=True)
dataset = pd.read_csv(dataset_file)
X = dataset.drop(columns=['Class']).values
y = dataset['Class'].values
print("DONE")

print("Calculating N1 ... ", end="", flush=True)
N1 = dcm.N1(X, y)
print("DONE")
print("N1 = {}".format(N1))
