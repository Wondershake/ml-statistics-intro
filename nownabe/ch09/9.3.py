import numpy as np
import random

def s2(seq):
    return ((seq - seq.mean()) ** 2).sum() / (seq.size - 1)

def S2(seq):
    return ((seq - seq.mean()) ** 2).sum() / seq.size

data = np.array([
    [
        0.3104913,
        0.3304700,
        0.0324358,
        0.8283330,
        0.1727581,
        0.6306326,
        0.7210595,
        0.2451280,
        0.7243750,
        0.8197760,
    ],
    [
        0.2753351,
        0.4359388,
        0.7160295,
        0.7775517,
        0.3251019,
        0.1736013,
        0.0921532,
        0.1318467,
        0.0642188,
        0.8002448,
    ],
    [
        0.3368585,
        0.2513685,
        0.2697405,
        0.1164189,
        0.3085003,
        0.2234060,
        0.9427391,
        0.5800890,
        0.7194922,
        0.8344245,
    ],
    [
        0.4086511,
        0.8016156,
        0.3221239,
        0.8498936,
        0.4362011,
        0.8559286,
        0.9982964,
        0.5540422,
        0.3757575,
        0.1312537,
    ],
    [
        0.4449823,
        0.1457471,
        0.9303545,
        0.1033269,
        0.4415264,
        0.5430776,
        0.8274743,
        0.3946336,
        0.8696082,
        0.6028266,
    ]
])

for _ in range(5):
    seq = []
    for _ in range(10):
        seq.append(random.random())

    data = np.append(data, [seq], axis=0)

for i in range(len(data)):
    seq = data[i]
    print(f"Sequence ({i+1})")
    print("s^2 = {0:0.4}, |sigma^2 - s^2| = {1:0.4}".format(s2(seq), np.abs(1/12 - s2(seq))))
    print("S^2 = {0:0.4}, |sigma^2 - S^2| = {1:0.4}".format(S2(seq), np.abs(1/12 - S2(seq))))
    print("")