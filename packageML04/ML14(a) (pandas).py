import numpy as np
import pandas as pd

s = pd.Series([1, 3, np.nan, 15, 7, 8])  # Single Dimensional array
# Even if a single value is float the entire array will become floating type
print(s)

dates = pd.date_range('20190101', periods=6, freq='D')  # yyyy-mm-dd format
# D means daily change, if M then dates will repeat along with month
print(dates)
print(dates[0])

print(np.random.randn(6, 4))  # Create a matrix of 6 rows 4 cols with random nos

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print("\n", df)
print("\nHeading in DataFrame : ", df.columns)
print("\nRow heading in data Frame", df.index)
print("\nValues in df = ", df.values)
print("\n", df.head())                                # Prints top 5 rows by default
print("\n", df.tail(3))                               # prints last 3 rows from data frame
print("\n", df.sample(3))                             # Selects randomly any 3

print("\n", df.describe())  # It gives the statistical summary of the data along the col. It tells if any data is missing

print("\n",df.describe(include='all'))    # Helpful when non-numeric data is also prst & we want the summary
                                          # else it will skip the column

print("\n",df.T)                                      # Transposing the data, external
print("\nSorted Values : \n",df.sort_values(by = 'B', ascending=True))   # by tell on the basis of which columns we have
                                                                        # to sort the data, External funct
