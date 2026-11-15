# Dataset Documentation

## 1. Dataset Overview

This project uses the Cleveland subset of the UCI Heart Disease dataset for binary classification.

The dataset contains clinical information collected from patients and is used to investigate the relationship between selected clinical features and the presence of recorded heart disease.

**Dataset details:**

| Property | Description |
|---|---|
| Dataset name | Heart Disease |
| Source | UCI Machine Learning Repository |
| Subset | Cleveland |
| File name | `processed.cleveland.data` |
| Total records | 303 |
| Input features | 13 |
| Original target variable | `num` |
| Original target classes | 0, 1, 2, 3, 4 |
| Missing values | 6 |

**Official dataset source:**

https://archive.ics.uci.edu/dataset/45/heart+disease

## 2. Dataset File

The project uses the processed Cleveland dataset file:

`data/raw/processed.cleveland.data`

The file contains comma-separated records without a header row. Column names are assigned during loading using Pandas.

The `?` symbol represents missing values in the original data file.

## 3. Dataset Features

The dataset contains 13 input features and one target variable.

| No. | Feature | Description | Type |
|---:|---|---|---|
| 1 | age | Age in years | Numerical |
| 2 | sex | Sex category | Categorical |
| 3 | cp | Chest pain type | Categorical |
| 4 | trestbps | Resting blood pressure | Numerical |
| 5 | chol | Serum cholesterol | Numerical |
| 6 | fbs | Fasting blood sugar category | Categorical |
| 7 | restecg | Resting electrocardiographic result | Categorical |
| 8 | thalach | Maximum heart rate achieved | Numerical |
| 9 | exang | Exercise-induced angina | Categorical |
| 10 | oldpeak | ST depression induced by exercise relative to rest | Numerical |
| 11 | slope | Slope of the peak exercise ST segment | Categorical |
| 12 | ca | Number of major vessels | Categorical |
| 13 | thal | Thalassemia-related category | Categorical |
| 14 | num | Original target variable | Target |

## 4. Feature Categories

For preprocessing, the 13 input features are separated into two groups.

### 4.1 Numerical Features

The following five features are processed using median imputation and StandardScaler:

- age
- trestbps
- chol
- thalach
- oldpeak

### 4.2 Categorical Features

The following eight features are processed using most-frequent imputation and OneHotEncoder:

- sex
- cp
- fbs
- restecg
- exang
- slope
- ca
- thal

The categorical feature values follow the coding scheme used in the original Cleveland dataset.

## 5. Missing Values

The dataset contains six missing values.

| Feature | Missing values |
|---|---:|
| ca | 4 |
| thal | 2 |
| **Total** | **6** |

Missing values are represented by `?` in the original dataset.

During loading, these values are converted into missing-value entries.

The preprocessing pipeline handles missing values as follows:

- Numerical features: Median imputation.
- Categorical features: Most-frequent-value imputation.

Imputation values are learned from the training data during model fitting.

## 6. Original Target Distribution

The original target variable is named `num` and contains five possible values.

The observed distribution in the 303 records is:

| Original target value | Number of records |
|---:|---:|
| 0 | 164 |
| 1 | 55 |
| 2 | 36 |
| 3 | 35 |
| 4 | 13 |
| **Total** | **303** |

## 7. Binary Target Conversion

For this project, the original five-class target is converted into a binary classification target.

The conversion is performed using:

`y = (df["num"] > 0).astype(int)`

The resulting classes are:

| Original target | Converted target | Meaning |
|---|---:|---|
| 0 | 0 | No disease recorded |
| 1 | 1 | Disease recorded |
| 2 | 1 | Disease recorded |
| 3 | 1 | Disease recorded |
| 4 | 1 | Disease recorded |

After conversion, the class distribution is:

| Binary class | Number of records |
|---|---:|
| 0 – No disease recorded | 164 |
| 1 – Disease recorded | 139 |
| **Total** | **303** |

This conversion changes the original multi-class classification problem into a binary classification problem.

## 8. Dataset Splitting

The dataset is divided into training and testing subsets using stratified sampling.

| Subset | Records | Proportion |
|---|---:|---:|
| Training | 242 | 80% |
| Testing | 61 | 20% |
| **Total** | **303** | **100%** |

The split uses a random state of 42 to make the experiment reproducible.

Stratification preserves approximately the original binary class proportions in both subsets.

## 9. Dataset Usage in the Project

The dataset is used for:

1. Inspecting records, data types, and missing values.
2. Separating input features and target values.
3. Converting the original target into two classes.
4. Fitting numerical and categorical preprocessing transformations.
5. Training the Logistic Regression classifier.
6. Evaluating model performance.
7. Extracting model coefficients for explainability.

The same dataset is also the basis for the interactive Flask prediction application.

## 10. Dataset Limitations

- The dataset contains only 303 records.
- It represents a historical Cleveland patient cohort.
- It may not represent the general population or other patient populations.
- Missing values are present in two categorical features.
- Dataset feature ranges should not be interpreted as medically established limits.
- The dataset alone cannot establish whether a model is clinically valid or suitable for medical diagnosis.

## 11. Ethical and Usage Considerations

The dataset is used for educational and machine-learning research purposes.

The classification output represents the model's prediction based on patterns learned from the historical dataset.

It should not be used as a substitute for professional medical advice, diagnosis, or clinical decision-making.

The probability displayed by the web application is the classifier's estimated probability for the positive class. It is not a calibrated personal clinical risk estimate.

## 12. Dataset Citation and License

**Dataset:** Heart Disease

**Source:** UCI Machine Learning Repository

**Original citation:**

Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). Heart Disease [Dataset]. UCI Machine Learning Repository.

https://doi.org/10.24432/C52P4X

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0).

The Cleveland dataset is used in this project for educational and machine-learning research purposes. The original dataset source is acknowledged, and the dataset has not been represented as an independently collected dataset.