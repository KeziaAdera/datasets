import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset (example: Iris dataset from seaborn's built-in datasets)
    df = sns.load_dataset('iris')  # You can replace this with pd.read_csv('your_dataset.csv')
    
    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check the structure of the dataset
    print("\nDataset Info:")
    print(df.info())

    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Clean the dataset (fill or drop missing values)
    df = df.dropna()  # Drop rows with missing values; alternatively, use df.fillna() to fill values
    print("\nDataset after cleaning:")
    print(df.info())

except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

    # Grouping by a categorical column and computing the mean
    grouped = df.groupby('species').mean()
    print("\nMean values grouped by species:")
    print(grouped)

    # Identify patterns
    print("\nObservations:")
    print("- Differences in mean petal length, petal width, etc., between species.")

except Exception as e:
    print(f"An error occurred during analysis: {e}")

# Task 3: Data Visualization
try:
    # Line chart (example dataset lacks time-series; we'll create a synthetic column)
    df['index'] = range(len(df))
    plt.figure(figsize=(8, 6))
    sns.lineplot(x='index', y='sepal_length', data=df, hue='species')
    plt.title("Line Chart: Sepal Length by Index")
    plt.xlabel("Index")
    plt.ylabel("Sepal Length")
    plt.legend(title="Species")
    plt.show()

    # Bar chart
    plt.figure(figsize=(8, 6))
    sns.barplot(x='species', y='petal_length', data=df, ci=None)
    plt.title("Bar Chart: Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length")
    plt.show()

    # Histogram
    plt.figure(figsize=(8, 6))
    sns.histplot(df['sepal_length'], kde=True, bins=15)
    plt.title("Histogram: Sepal Length Distribution")
    plt.xlabel("Sepal Length")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='sepal_length', y='petal_length', hue='species', style='species', data=df)
    plt.title("Scatter Plot: Sepal Length vs. Petal Length")
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Length")
    plt.legend(title="Species")
    plt.show()

except Exception as e:
    print(f"An error occurred during visualization: {e}")
