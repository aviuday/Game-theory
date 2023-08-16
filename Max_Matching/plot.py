# importing pandas library
import pandas as pd
# import matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.read_csv('output.csv')
print(df)

avg = 0

for i in df.index:
    ttc = df["Max Matching"][i]
    rnd = df[" Random"][i]
    improvement = ((ttc-rnd)/rnd)*100
    avg += improvement

avg /= 10
print("Improvement = " + str(avg) + "%")

df.plot(kind="bar")
plt.show()

