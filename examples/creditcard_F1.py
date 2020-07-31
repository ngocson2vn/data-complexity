import json
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

print("Calculating F1 ... ", end="", flush=True)
ratios, F1 = dcm.F1(X, y)
print("DONE")
print("F1 = {}".format(F1))
print("Discriminant Ratios = {}".format(json.dumps(ratios, indent=2)))
