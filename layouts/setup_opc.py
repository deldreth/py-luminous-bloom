#!/usr/bin/env python

import json

data = []
offset = 0.05
coords = [
    (0.1, 0),
    (0.05, 0.1),
    (-0.05, 0.1),
    (-0.1, 0),
    (-0.05, -0.1),
    (0.05, -0.1),
]
for x, y in coords:
    total = 0

    for p in range(64):
        data.append({
            'point': [x, y, round(total, 2)]
        })
        total += offset

with open('./layouts/opc.json', 'w') as outfile:
    json.dump(data, outfile)
