from DA_test import * 
from similarity import *
from workload import * 
import random

capacity = num_mentees/num_mentors

total_utility_da = 0 
mentor_utility_da = 0
mentee_utility_da = 0


for i in allocation: 
    # print(similarity_matrix[int(i)][allocation[i]], workload_matrix[allocation[i]][int(i)])
    mentor_utility_da += workload_matrix[allocation[i]][int(i)]
    mentee_utility_da += similarity_matrix[int(i)][allocation[i]]


total_utility_da = mentee_utility_da + mentor_utility_da/capacity

# print(mentee_utility_da)
print((mentor_utility_da))

random_allocation = {}

mentee_number = list(range(num_mentees))
random.shuffle(mentee_number)
# print(mentee_number)
for i in range(len(mentee_number)):
    random_allocation[str(mentee_number[i])] = i % num_mentors

# print(allocation)
# print(random_allocation)

better_mentor = 0
worse_mentor = 0

for i in range(len(mentee_number)):
    if similarity_matrix[i][random_allocation[str(mentee_number[i])]] > similarity_matrix[i][allocation[str(mentee_number[i])]]:
        worse_mentor += 1
    else: 
        better_mentor += 1

total_utility_random = 0
mentor_utility_random = 0
mentee_utility_random = 0 

for i in random_allocation: 
    mentor_utility_random += workload_matrix[random_allocation[i]][int(i)]
    mentee_utility_random += similarity_matrix[int(i)][random_allocation[i]]

total_utility_random = mentee_utility_random + mentor_utility_random/capacity


print(abs(mentor_utility_random))


# print(mentor_utility_da, mentor_utility_random)
# print(mentee_utility_da, mentee_utility_random)
