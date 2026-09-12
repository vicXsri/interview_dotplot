import csv
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pointbiserialr

input_file = "breast+cancer+wisconsin+original/breast-cancer-wisconsin.csv"
output_file = "breast+cancer+wisconsin+original/breast-cancer-wisconsin-scored.csv"

scores = []
classes = []

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:

        # Remove rows where Clump Thickness = 1
        if row[1] == "1":
            continue

        # Remove rows containing missing values
        if "?" in row:
            continue

        # Attributes 2-10
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

        # Arithmetic mean
        score = sum(attributes) / len(attributes)

        # Class = Attribute 11
        class_value = int(row[10])

        # Store values for correlation later
        scores.append(score)
        classes.append(class_value)

        # Add the mean score to the 
        row.append(round(score, 2))

        #write into the rows of the CSV File !
        writer.writerow(row)

# Select the method
print("\nSelect correlation method:")
print("0 - Both")
print("1 - Spearman correlation")
print("2 - Point-biserial correlation")

choice = input("\nEnter the method number: ")

#run the req lines acc to the choice
if choice == "0":
    correlation_spearman, p_value = spearmanr(scores, classes)
    print("\nSpearman Correlation Result")
    print("---------------------------")
    print("Correlation:", correlation_spearman)

    correlation_pointbiserial, p_value = pointbiserialr(classes, scores)
    print("\nPoint-Biserial Correlation Result")
    print("---------------------------------")
    print("Correlation:", correlation_pointbiserial)

elif choice == "1":

    correlation_spearman, p_value = spearmanr(scores, classes)

    print("\nSpearman Correlation Result")
    print("---------------------------")
    print("Correlation:", correlation_spearman)

elif choice == "2":

    correlation_pointbiserial, p_value = pointbiserialr(classes, scores)

    print("\nPoint-Biserial Correlation Result")
    print("---------------------------------")
    print("Correlation:", correlation_pointbiserial)

else:

    print("\nInvalid option. Please enter 1 or 2.")


benign_scores = []
malignant_scores = []

#store the scores individually
for i in range(len(classes)):

    if classes[i] == 2:
        benign_scores.append(scores[i])

    elif classes[i] == 4:
        malignant_scores.append(scores[i])


benign_average = sum(benign_scores) / len(benign_scores)
malignant_average = sum(malignant_scores) / len(malignant_scores)

#make a plt
plt.figure()

#this is a bar graph
plt.bar(
    ["Benign", "Malignant"],
    [benign_average, malignant_average]
)
#add the lable and titles
plt.xlabel("Class")
plt.ylabel("Average Predicted Score")
plt.title("Average Predicted Score by Class")

#tell the axis
plt.grid(axis="y")

#store the image along with the data
plt.savefig(
    "breast+cancer+wisconsin+original/average-score-by-class.png",
    dpi=300,
    bbox_inches="tight"
)

#close the plot
plt.close()

print("Graph saved successfully")