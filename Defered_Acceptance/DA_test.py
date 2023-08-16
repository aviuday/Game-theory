from mentee_pref import * 
from mentor_pref import * 
from deffered_acceptance import * 

allocation = deferred_acceptance(mentee_pref, mentor_pref)

for i in allocation: 
   allocation[i] = allocation[i]//capacity

