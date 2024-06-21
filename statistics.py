# Import the libraries
import warnings
import pandas as pd
import numpy as np
import scipy.stats as stats

warnings.simplefilter(action='ignore', category=FutureWarning)

# Load the dataset from a csv file
df = pd.read_csv("output.csv",
                 sep='\t',
                 skiprows=1,
                 names=['Frequency', 'Types'],)
# Set values in the column 'Type' as index names
df1 = df.set_index('Types')
print(df1)
print()
print()

# Get the summary statistics using pandas
df1.describe()

# Get the mean of each column using numpy
mean = np.mean(df1)

# Get the median of each column using numpy
median = np.median(df1)

# Get the standard deviation of each column using numpy
standard_deviation = int(np.std(df1, axis=0))

# Get the variance of each column using numpy
variance = int(np.var(df1, axis=0))

# Get the skewness of each column using scipy
skewness = stats.skew(df1, axis=0)

# Get the kurtosis of each column using scipy
kurtosis = stats.kurtosis(df1, axis=0)

df2 = pd.DataFrame({'R-E-S-U-L-T-S': [round(mean, 2), round(median, 2), round(standard_deviation, 2), round(variance, 2), skewness, kurtosis]},
                   index=(['MEAN', 'MEDIAN', 'STANDARD DEVIATION', 'VARIANCE', 'SKEWNESS', 'KURTOSIS']))
print(df2)
