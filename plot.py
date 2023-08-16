# # importing pandas library
import pandas as pd
# import matplotlib library
import matplotlib.pyplot as plt
import numpy as np 

# # creating dataframe
df1 = pd.read_csv('output1.csv')
df2 = pd.read_csv('output2.csv')
df3 = pd.read_csv('output3.csv')
df4 = pd.read_csv('output4.csv')
df5 = pd.read_csv('output5.csv')
# print(df)
# print(list(df))
mentor_utility_da1 = df1["Mentor-Utility-DA"].to_numpy()
mentor_utility_random1 = df1[" Mentor-Utility-Random"].to_numpy()
mentor_utility_da2 = df2["Mentor-Utility-DA"].to_numpy()
mentor_utility_random2 = df2[" Mentor-Utility-Random"].to_numpy()
mentor_utility_da3 = df3["Mentor-Utility-DA"].to_numpy()
mentor_utility_random3 = df3[" Mentor-Utility-Random"].to_numpy()
mentor_utility_da4 = df4["Mentor-Utility-DA"].to_numpy()
mentor_utility_random4 = df4[" Mentor-Utility-Random"].to_numpy()
mentor_utility_da5 = df5["Mentor-Utility-DA"].to_numpy()
mentor_utility_random5 = df5[" Mentor-Utility-Random"].to_numpy()

inc1 = (mentor_utility_da1 - mentor_utility_random1)*100/mentor_utility_random1
inc2 = (mentor_utility_da2 - mentor_utility_random2)*100/mentor_utility_random2
inc3 = (mentor_utility_da3 - mentor_utility_random3)*100/mentor_utility_random3
inc4 = (mentor_utility_da4 - mentor_utility_random4)*100/mentor_utility_random4
inc5 = (mentor_utility_da5 - mentor_utility_random5)*100/mentor_utility_random5

# DA = df["DA"].to_numpy()
# Max_Matching = df[" Max-Matching"].to_numpy()
# Top_Trading_Cycle = df[" Top-Trading-Cycle"].to_numpy()
# Random = df[" Random-TTC"].to_numpy()
# better_da = df[" Better-DA"].to_numpy()
# worse_da = df[" Worse-DA"].to_numpy()
# better_mm = df[" Better-MM"].to_numpy()
# worse_mm = df[" Worse-MM"].to_numpy()
# better_ttc = df[" Better-TTC"].to_numpy()
# worse_ttc = df[" Worse-TTC"].to_numpy()

# DA_Normalized = np.divide((DA - Random), Random)*100
# Max_Matching_Normalized = np.divide((Max_Matching - Random), Random)*100
# Top_Trading_Cycle_Normalized = np.divide((Top_Trading_Cycle - Random), Random)*100

# array1 = DA_Normalized
# array2 = Max_Matching_Normalized
# array3 = Top_Trading_Cycle_Normalized

# calculate the means and variances of the arrays

# mean_da_mu = abs(np.mean(mentor_utility_da))
# mean_rd_mu = abs(np.mean(mentor_utility_random))
# print(mean_da_mu - mean_rd_mu)
# mean1 = np.mean(array1)
# mean2 = np.mean(array2)
# mean3 = np.mean(array3)

# var_da = np.var(mentor_utility_da)
# var_rd = np.var(mentor_utility_random)

# var1 = np.var(array1)
# var2 = np.var(array2)
# var3 = np.var(array3)

# mean_better_da = np.mean(better_da)
# mean_worse_da = np.mean(worse_da)
# mean_better_mm = np.mean(better_mm)
# mean_worse_mm = np.mean(worse_mm)
# mean_better_ttc = np.mean(better_ttc)
# mean_worse_ttc = np.mean(worse_ttc)

# create a bar graph of the means

# Define the data
data = [np.mean(inc1), np.mean(inc2), np.mean(inc3), np.mean(inc4), np.mean(inc5)]

# Define the x-axis labels
# labels = ['Variable 1', 'Variable 2', 'Variable 3', 'Variable 4', 'Variable 5']
labels = ['50/500', '100/500', '10/100', '70/490', '80/640']

# Define the colors for the bars
# colors = ['coral', 'coral', 'coral', 'coral', 'coral']
colors = ['#4286f4', '#0097f2', '#316ab1', '#00a1ff', '#0077b6'] #00a1ff

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data as a bar graph
ax.bar(labels, data, color=colors)

# Set the title and axis labels
ax.set_xlabel('Number of Mentors/Mentees')
ax.set_ylabel('Percentage increase in utility of mentors')

# Show the plot
plt.show()

# Define the data
data = [inc1, inc2, inc3, inc4, inc5]

# Define the x-axis labels
labels = ['50/500', '100/500', '10/100', '70/490', '80/640']

# Define the colors for the bars
colors = ['red', 'blue', 'green', 'orange', 'purple']

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data as a bar graph
ax.bar(labels, data, color=colors)

# Set the title and axis labels
# ax.set_title('Bar Graph')
ax.set_xlabel('Number of Mentors/Mentees')
ax.set_ylabel('Percentage increase in utility of mentors')

# Show the plot
plt.show()
