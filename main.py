import os 

if os.path.isfile("mock_data.csv"):
    print("file exists")
    import pandas as pd 
    df = pd.read_csv("mock_data.csv")
    df.to_json('run.log',orient='records',indent=4)

