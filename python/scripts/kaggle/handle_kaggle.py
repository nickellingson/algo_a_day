import pandas as pd

# handle kaggle dataset
def read_kaggle_csv(file_path):
    with open(file_path, "r") as f:
        df = pd.read_csv(f)
        return df
# remove missing
def handle_kaggle_csv(df):
    # print(df.head())
    # print(df.info())
    # print(df.describe())
    df.dropna(inplace=True)
    return df

# mean life expectancy for each age
def analyze_data(df):
    summary = df.groupby("Year").agg({'Period life expectancy at birth': 'mean'})
    return summary

start_df = read_kaggle_csv("./life-expectancy.csv")
print(start_df)

rm_na_df = handle_kaggle_csv(start_df)
print(rm_na_df.head())

analyze_data_df = analyze_data(rm_na_df)
print(analyze_data_df)

# process chunks of data with file read
def process_chunk(path):
    with open(path, "r") as f:
        count = 1
        for chunk in pd.read_csv(path, chunksize=10):
            print("new chunk")
            print(chunk)
            count += 1
            if count == 5:
                break
process_chunk("./life-expectancy.csv")