import pandas as pd

# Define the path to the file
file_path = 'datasets/2018 Faculty MISO Survey Results.csv'

# Load the dataset into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())