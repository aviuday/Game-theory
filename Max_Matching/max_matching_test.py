from graph import *
from dlib_max_matching import *
from mentees_preference import *


# integers are houses, chars are agents
mentees = {str(i) for i in range(num_mentees)}
mentors = set(range(num_mentees))
allocation = minCost(dlib.matrix(similarity_matrix))
# print(allocation)
for i in allocation: 
   allocation[i] = allocation[i]//capacity

   



