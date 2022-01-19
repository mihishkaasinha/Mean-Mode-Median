import statistics
import pandas as pd

df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()
median = statistics.median(data)
mode = statistics.mode(data)
mean = statistics.mean(data)

print("The Mean: " + mean)
print("The Mode: " + mode)
print("The Median: " + median)