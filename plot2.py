# # importing pandas library
import pandas as pd
# import matplotlib library
import matplotlib.pyplot as plt
import numpy as np 

# # creating dataframe
df = pd.read_csv('output.csv')


DA = df["DA"].to_numpy()
Max_Matching = df[" Max-Matching"].to_numpy()
Top_Trading_Cycle = df[" Top-Trading-Cycle"].to_numpy()
Random = df[" Random-TTC"].to_numpy()
better_da = df[" Better-DA"].to_numpy()
worse_da = df[" Worse-DA"].to_numpy()
better_mm = df[" Better-MM"].to_numpy()
worse_mm = df[" Worse-MM"].to_numpy()
better_ttc = df[" Better-TTC"].to_numpy()
worse_ttc = df[" Worse-TTC"].to_numpy()

DA_Normalized = np.divide((DA - Random), Random)*100
Max_Matching_Normalized = np.divide((Max_Matching - Random), Random)*100
Top_Trading_Cycle_Normalized = np.divide((Top_Trading_Cycle - Random), Random)*100

array1 = DA_Normalized
array2 = Max_Matching_Normalized
array3 = Top_Trading_Cycle_Normalized

# calculate the means and variances of the arrays

mean1 = np.mean(array1)
mean2 = np.mean(array2)
mean3 = np.mean(array3)
var1 = np.var(array1)
var2 = np.var(array2)
var3 = np.var(array3)

mean_better_da = np.mean(better_da)
mean_worse_da = np.mean(worse_da)
mean_better_mm = np.mean(better_mm)
mean_worse_mm = np.mean(worse_mm)
mean_better_ttc = np.mean(better_ttc)
mean_worse_ttc = np.mean(worse_ttc)

# create a bar graph of the means

means = [mean1, mean2, mean3]
labels = ['DA', 'Max Matching', 'Top Trading Cycle']
x_pos = np.arange(len(means))
bar_width = 0.5
plt.bar(x_pos, means, width=bar_width, align='center', color=['blue', 'orange', 'green'])
plt.xticks(x_pos, labels)
plt.ylabel('Mean')

# add error bars to show the variances
yerr = [var1, var2, var3]
plt.errorbar(x_pos, means, yerr=yerr, fmt='none', capsize=5, ecolor='red', elinewidth=2*bar_width)

# display the graph
plt.title("Change in Mentor Workload (out of 100)")
plt.show()


a1 = [mean_better_da/5, mean_better_mm/5, mean_better_ttc/5]
a2 = [mean_worse_da/5, mean_worse_mm/5, mean_worse_ttc/5]

x = np.arange(len(a1))

# Set the width of each bar
width = 0.2

# Set the colors for each iteration
colors = ['#4286f4', '#316ab1', '#ff6347']

# Create the bar chart
plt.bar(x - width, a1, width, color=colors[0], label='Iteration 1')
plt.bar(x, a2, width, color=colors[1], label='Iteration 2')

# Add a title and labels for the x and y axes
plt.title('Comparison of Better off and Worse off')
plt.ylabel('Count %')

# Set the x-axis tick labels to be the index of each element
plt.xticks(x, ['DA', 'Max Matching', 'Top Trading Cycle'])


# Show the chart
plt.show()