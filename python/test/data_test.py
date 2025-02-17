# read files from json folder and create dataframes
import os
import pandas as pd
import json

# read json files out of folder
def read_json_files():
    print(os.getcwd())
    result = []
    for root, _, files in os.walk("./json"):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, "r") as f:
                df = pd.read_json(f) 
            # or  
            #     data = json.load(f)
            # df = pd.DataFrame(data)
            result.append(df)
    return result

print(res := read_json_files())

# walk over list and manipulate df
def walk_df_list(list):
    for i, df in enumerate(list):
        print(f"DF {i}")
        print(df.head())

walk_df_list(res)



# dataframe operations





# numpy