# importing pandas library
import pandas as pd
# import matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.read_csv('output.csv')
print(df)

df.plot(kind="bar")
plt.show()


