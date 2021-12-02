import pandas as pd
import datetime

if __name__ == '__main__':
    print("hello")
    additions = pd.read_csv("data/addition.csv")
    additions["result"] = additions["value1"] + additions["value2"]
    additions["timestamp"] = datetime.datetime.now()
    additions.to_csv("processed_data/processed_operations", mode="a", index=False, header = False)
