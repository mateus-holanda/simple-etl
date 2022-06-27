import requests
import ndjson
import pandas as pd

source1 = "http://208.167.255.20:8080/primer/2022_01_03.json.txt"
source2 = "http://208.167.255.20:8080/primer/2022_01_04.json.txt"
source3 = "http://208.167.255.20:8080/primer/2022_01_05.json.txt"


def extract_data_from_url(url, filename):
  response = requests.get(url)
  data = ndjson.loads(response.text)
  with open(f'./data/{filename}.ndjson', 'w') as f:
    ndjson.dump(data, f)


def main():
  print("[Extract] Start")

  print("[Extract] Extracting data from first source...")
  extract_data_from_url(source1, "source1")

  print("[Extract] Extracting data from second source...")
  extract_data_from_url(source2, "source2")

  print("[Extract] Extracting data from third source...")
  extract_data_from_url(source3, "source3")
  
  print("[Extract] End.")