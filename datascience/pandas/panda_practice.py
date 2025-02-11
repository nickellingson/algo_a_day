import pandas as pd
df = pd.read_csv("data.csv")  # Also supports Excel, Parquet, SQL, etc.

print(df.head())        # First 5 rows
print(df.info())        # Schema and non-null counts
print(df.describe())    # Summary statistics

df.fillna(0, inplace=True)  # Replace NaNs with 0
df.dropna(inplace=True)     # Drop rows with NaNs

df.rename(columns={"old_name": "new_name"}, inplace=True)

df["column_name"] = df["column_name"].astype("int")

df["new_column"] = df["old_column"].apply(lambda x: x * 2)

grouped = df.groupby("category")["value"].sum()

merged = pd.merge(df1, df2, on="key_column", how="inner")

for chunk in pd.read_csv("large_file.csv", chunksize=10000):
    process(chunk)


df["rank"] = df.groupby("department")["salary"].rank(method="dense", ascending=False)

df["running_total"] = df["sales_amount"].cumsum()


# Load your dataset
df = pd.read_csv("filepath")

# Option 1: Drop categorical columns if they're not needed
df = df.drop(columns=['Country'])  # replace 'Country' with the actual column name if it's not required

# Option 2: Convert categorical columns to numeric using one-hot encoding
df = pd.get_dummies(df, columns=['Country'])  # replace 'Country' with the column that contains 'Lebanon'

# Then proceed to split and train your model