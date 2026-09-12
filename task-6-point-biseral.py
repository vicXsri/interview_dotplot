import csv
from scipy.stats import pointbiserialr

classes = []
scores = []

with open("breast+cancer+wisconsin+original/breast-cancer-wisconsin-weighted-score.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        classes.append(int(row[10]))
        scores.append(float(row[11]))

correlation, p_value = pointbiserialr(scores, classes)

print("Point-biserial correlation:", correlation)