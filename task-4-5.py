import csv

input_file = "breast+cancer+wisconsin+original/breast-cancer-wisconsin-cleaned-clump-thickness-1-?.csv"
output_file = "breast+cancer+wisconsin+original/breast-cancer-wisconsin-weighted-score.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:

        attributes = [
            int(row[1]),
            int(row[2]),
            int(row[3]),
            int(row[4]),
            int(row[5]),
            int(row[6]),
            int(row[7]),
            int(row[8]),
            int(row[9])
        ]

        score = sum(attributes) / len(attributes)

        row.append(round(score, 2))

        writer.writerow(row)

print("Scored CSV created")