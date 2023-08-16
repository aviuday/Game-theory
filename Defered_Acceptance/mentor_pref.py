from workload import * 

#sort every row, first keep hashmap with key as prob: value as index
capacity = num_mentees//num_mentors

mentor_pref = {}
no_mentors = len(workload_matrix)
for mentor in range(no_mentors):
    pref = []
    value_to_index = {}
    for i in range(len(workload_matrix[mentor])):
        key = round(workload_matrix[mentor][i], 9)
        if key in value_to_index:
            value_to_index[key].append(i)
        else: value_to_index[key] = [i]
    sorted_values = sorted(value_to_index.keys(), reverse=True)
    for i in sorted_values:
        for j in value_to_index[i]:
            pref.append(str(j)) #1 plus index
            # for k in range(capacity):         
            #     pref.append(capacity*j + k) #hashing
    for k in range(capacity):
        mentor_pref[capacity*mentor+k] = pref

