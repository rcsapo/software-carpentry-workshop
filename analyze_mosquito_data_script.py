import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

filename = "A1_mosquito_data.csv"

# Read in data
data = pd.read_csv(filename)
print data.head()

# Convert temperatures from Fahrenheit to Celsius
data["temperature"] = (data["temperature"] - 32) * 5/9
print data.head()

# Call analyze function to analyze data



