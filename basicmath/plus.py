import json

dataset = []

for i in range(1, 21):
    for j in range(1, 21):
        prompt = "Basic math expression with plus"
        completion = f"Evalute this expression: {i}+{j}"
        data = {"prompt": prompt, "completion": completion}
        dataset.append(data)

with open("../plus.json", "w") as f:
    for data in dataset:
        f.write(json.dumps(data) + "\n")
