from similarity import * 

#sort every row, first keep hashmap with key as prob: value as index
capacity = num_mentees//num_mentors

mentee_pref = {}
no_mentees = len(similarity_matrix)
for mentee in range(no_mentees):
    pref = []
    value_to_index = {}
    for i in range(len(similarity_matrix[mentee])):
        key = round(similarity_matrix[mentee][i], 9)
        if key in value_to_index:
            value_to_index[key].append(i)
        else: value_to_index[key] = [i]
    sorted_values = sorted(value_to_index.keys(), reverse=True)
    for i in sorted_values:
        for j in value_to_index[i]:
            for k in range(capacity):         
                # pref.append(j+1) #1 plus index
                pref.append(capacity*j + k) #hashing
    mentee_pref[str(mentee)] = pref

