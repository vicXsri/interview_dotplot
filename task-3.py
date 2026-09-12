import csv

input_file = "breast+cancer+wisconsin+original/breast-cancer-wisconsin.csv"
output_file = "breast+cancer+wisconsin+original/breast-cancer-wisconsin-cleaned-clump-thickness-1-?.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:

        if row[1] == "1":
            continue
        if "?" in row:
            continue    
        
        writer.writerow(row)

print("Cleaned copy created")