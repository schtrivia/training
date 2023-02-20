import glob

pattern = "*.jsonl"

output_file = "main.jsonl"

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in glob.glob(pattern):
        if filename != output_file:
            with open(filename, "r", encoding="utf-8") as infile:
                text = infile.read()
                outfile.write(text)
                outfile.write("\n")
