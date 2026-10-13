
import pandas as pd

# Load the student dataset
df = pd.read_csv("students.csv")

print("FIRST FIVE STUDENT RECORDS")
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# Fill missing numerical values with their column medians
numeric_columns = [
    "gpa",
    "attendance",
    "study_hours",
    "failed_courses"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing support labels with the most common label
df["support_level"] = df["support_level"].fillna(
    df["support_level"].mode()[0]
)

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# Save the cleaned dataset
df.to_csv("students_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
