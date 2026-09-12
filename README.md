This project analyses the Breast Cancer Wisconsin (Original) dataset using Python. It cleans the source data, calculates a simple predicted score from the diagnostic attributes, measures the relationship between that score and the tumour class, and visualises the average score for benign and malignant samples.

## Dataset

The original dataset contains **699 cases**. Each row includes an ID, nine diagnostic attributes, and a class label:

- `2` - benign
- `4` - malignant

The source `.data` file uses comma-separated values but does not contain column headings. The attribute order was taken from the accompanying `.names` file, and a CSV copy was used for the analysis.

## Data cleaning

Two filters were applied before calculating the scores:

1. Rows containing `?` were removed. There were **16 missing values**, all in the Bare Nuclei column.
2. Rows where Clump Thickness was equal to `1` were removed, as required by the assessment.

After filtering, the dataset was reduced from **699 to 541 samples**.

## Predicted score

The ID and class columns were excluded from the score. For every remaining row, the score was calculated as the arithmetic mean of the nine diagnostic attributes:

```text
predicted score = sum(attributes 2 to 10) / 9
```

The calculated value was rounded to two decimal places and appended to the output CSV as a twelfth column.

During exploratory comparison, scores below approximately `3` were generally associated with benign samples, while scores above approximately `3` were generally associated with malignant samples.

## Correlation methods

Two correlation methods were selected:

- **Spearman correlation** measures whether higher predicted scores generally occur with the higher class value without assuming a perfectly linear relationship.
- **Point-biserial correlation** measures the relationship between the continuous predicted score and the two class groups, benign and malignant.

The program allows the user to calculate either method individually or both together.

## Results

| Method | Correlation coefficient |
| --- | ---: |
| Spearman | `0.8482002870320052` |
| Point-biserial | `0.8895973139680835` |

Both coefficients are close to `+1`, indicating a strong positive relationship between the predicted score and class. In this dataset, malignant samples generally received higher predicted scores than benign samples.

## Visualisation

The bar chart compares the average predicted score for the two classes.

![Average predicted score by class](Final%20Results/average-score-by-class.png)

## Analysis workflow

1. Read the Breast Cancer Wisconsin CSV data.
2. Remove rows where Clump Thickness is `1`.
3. Remove rows containing a missing value (`?`).
4. Calculate the mean of attributes 2-10 for each retained row.
5. Append the predicted score to the output CSV.
6. Calculate Spearman and/or point-biserial correlation.
7. Calculate the average score for each class and save the bar chart as a PNG.

## Running the program

The project requires Python with Matplotlib and SciPy installed.

```bash
pip install matplotlib scipy
python main.py
```

When prompted, enter:

- `0` to run both correlation methods
- `1` to run Spearman correlation
- `2` to run point-biserial correlation

## References

- [Python 3.11 documentation](https://docs.python.org/3.11/)
- [Python `csv` module](https://docs.python.org/3/library/csv.html)
- [SciPy user guide](https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide)
- [Matplotlib user guide](https://matplotlib.org/stable/users/index.html)
