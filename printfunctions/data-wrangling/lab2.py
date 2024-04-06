import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen

def download(url, filename):
    with urlopen(url) as response:
        with open(filename, "wb") as f:
            f.write(response.read())

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

download(filename, "auto.csv")
df = pd.read_csv("auto.csv", names=headers)


print(df.head())
