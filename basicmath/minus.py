import json
import random

dataset = []

for i in range(1, 21):
    for j in range(1, 21):
        prompt = "Basic math expression with minus"
        x, y = sorted([i, j])
        completion = f"Evalute this expression: {y}-{x}"
        data = {"prompt": prompt, "completion": completion}
        dataset.append(data)

with open("../minus.json", "w") as f:
    for data in dataset:
        f.write(json.dumps(data) + "\n")
