import os
import requests
from tqdm import tqdm

def download_creditcard(dataset_file):
  if os.path.isfile(dataset_file) and os.stat(dataset_file).st_size > 0:
    return
  url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"
  response = requests.get(url, stream=True)
  response.raise_for_status()
  filesize = int(response.headers.get('content-length', 0))
  p = tqdm(total=filesize, unit='iB', unit_scale=True)
  with open(dataset_file, "wb") as fd:
    for chunk in tqdm(response.iter_content(chunk_size=1024)):
      if chunk:
        fd.write(chunk)
        p.update(len(chunk))
  p.close()
  if filesize != 0 and p.n != filesize:
    print("ERROR, something went wrong")