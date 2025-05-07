This project involves performing data analysis and visualization using Python. We use the Iris dataset (or any other CSV dataset of your choice) to demonstrate how to:

Load and clean a dataset

Perform basic statistical analysis

Explore the data with groupings

Visualize patterns using different types of plots

Dataset
We use a dataset in CSV format. The Iris dataset is provided by default via sklearn.datasets, but any other dataset from Kaggle or UCI ML Repository may also be used.


Task Breakdown
 Task 1: Load and Explore the Dataset
   Load the dataset using pandas
   Display the first few rows using .head()
   Inspect the data types and check for missing values
   Clean the dataset:
   Fill or drop missing values as needed
Error handling for file operations using try-except

 Task 2: Basic Data Analysis
Compute statistical metrics using .describe():

Mean, median, standard deviation, etc.

Group data based on a categorical column (e.g., species)

Compute mean for each group

Identify and summarize patterns or insights

 Task 3: Data Visualization
Four different types of visualizations are created:

Line Chart – To show trends over time (e.g., time-series sales)

Bar Chart – Comparison across categories (e.g., average petal length per species)

Histogram – To visualize the distribution of a numeric column

Scatter Plot – To show relationships between two numerical columns
