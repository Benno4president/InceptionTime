import sys, os
import argparse
import pandas as pd

def load_dataset(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        data = pd.read_csv(f, sep=',', header=None)
        data = data.replace(r';', '', regex=True)
    return data

def main():
    sample_rate = 100
    dataset = load_dataset('./SisFall_dataset/SA01/D01_SA01_R01.txt')
    print(dataset)
    converted_dataset = []
    datapoint = ''
    for i in dataset.to_dict():
        if not (i % sample_rate) == 1:


if __name__ == "__main__":
    main()