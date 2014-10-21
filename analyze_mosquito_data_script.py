import pandas as pd
import matplotlib.pyplot as plt

import analyze_mosquito_data_lib as mosquito_lib

filename = "A1_mosquito_data.csv"

# Read in data
data = pd.read_csv(filename)
print data.head()

# Convert temperatures from Fahrenheit to Celsius calling function form mosquito_lib
data["temperature"] = mosquito_lib.fahr_to_celsius(data["temperature"])
print data.head()

# Call analyze function to analyze data
parameters = mosquito_lib.analyze(data,"plot.png")
print parameters

# Write results to .csv
parameters.to_csv("parameters.csv")

# Create and save plot
# plt.savefig()