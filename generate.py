import glob

pattern = "*.json"

output_file = "main.json"

with open(output_file, "w") as outfile:

    for filename in glob.glob(pattern):

        if filename != output_file:

            with open(filename, "r") as infile:

                text = infile.read()

                outfile.write(text)

                outfile.write("\n")


