from max_matching_test import * 
from similarity import *
import random

total_similarity_max_matching = 0 

for i in allocation: 
    total_similarity_max_matching += similarity_matrix[int(i)][allocation[i]*capacity]

print(total_similarity_max_matching)

random_allocation = {}

mentee_number = list(range(num_mentees))
random.shuffle(mentee_number)
# print(mentee_number)
for i in range(len(mentee_number)):
    random_allocation[str(mentee_number[i])] = i % num_mentors

# print(random_allocation)

total_similarity_random = 0

for i in random_allocation: 
    total_similarity_random += similarity_matrix[int(i)][random_allocation[i]*capacity]



print(total_similarity_random)

better_mentor = 0
worse_mentor = 0

for i in range(len(mentee_number)):
    if similarity_matrix[i][random_allocation[str(mentee_number[i])]] > similarity_matrix[i][allocation[str(mentee_number[i])]]:
        worse_mentor += 1
    else: 
        better_mentor += 1

print(better_mentor)
print(worse_mentor)
