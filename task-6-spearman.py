import csv
from scipy.stats import spearmanr

classes = []
scores = []

with open("breast+cancer+wisconsin+original/breast-cancer-wisconsin-weighted-score.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        classes.append(int(row[10]))
        scores.append(float(row[11]))

correlation, p_value = spearmanr(scores, classes)

print("Spearman correlation:", correlation)