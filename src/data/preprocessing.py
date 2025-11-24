import pandas as pd
import os

# Get folder where this script lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build full path to CSV
csv_path = os.path.join(script_dir, "student-scores.csv")

# Read CSV
df = pd.read_csv(csv_path)

# print(df.head())
print(df.isna().sum())