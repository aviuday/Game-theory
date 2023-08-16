import sys

from GT_data import *

def workload(mentor, mentee):

    cpi1 = mentor.CPI
    cpi2 = mentee.CPI
    
    if cpi1 >= 9.5: 
        class1 = 7
    elif cpi1 >= 8.5: 
        class1 = 6
    elif cpi1 >= 7.5:
        class1 = 5
    elif cpi1 >= 6.5: 
        class1 = 4
    elif cpi1 >= 5.5:
        class1 = 3
    elif cpi1 >= 4: 
        class1 = 2 
    else: 
        class1 = 1

    if cpi2 >= 9.5: 
        class2 = 7
    elif cpi2 >= 8.5: 
        class2 = 6
    elif cpi2 >= 7.5:
        class2 = 5
    elif cpi2 >= 6.5: 
        class2 = 4
    elif cpi2 >= 5.5:
        class2 = 3
    elif cpi2 >= 4: 
        class2 = 2 
    else: 
        class2 = 1

    cpi_similarity = min((1 - (class1 - class2)/6), 1)

    free = 4 
    if mentee.diff['Depression']: 
        if mentor.diff['Depression']:
            free -= 0.5
        else: 
            free -= 1
    if mentee.diff['DAC']: 
        if mentor.diff['DAC']:
            free -= 0.5
        else: 
            free -= 1
    if mentee.diff['S_Anxiety']: 
        if mentor.diff['S_Anxiety']:
            free -= 0.5
        else: 
            free -= 1
    if mentee.diff['DX/FR']: 
        if mentor.diff['DX/FR']:
            free -= 0.5
        else: 
            free -= 1
    free /= 4

    interests_similarity = 4 

    if mentee.interest['Sports'] and not mentor.interest['Sports']: 
        interests_similarity -= 1
    if mentee.interest['Cult'] and not mentor.interest['Cult']: 
        interests_similarity -= 1
    if mentee.interest['Tech'] and not mentor.interest['Tech']: 
        interests_similarity -= 1
    if mentee.interest['Acads'] and not mentor.interest['Acads']: 
        interests_similarity -= 1
    
    interests_similarity /= 4
    


    return (0.2*cpi_similarity + 0.5*free + 0.3*interests_similarity)

workload_matrix = [[0]*num_mentees for i in range(num_mentors)]


# TODO Make sure workload_matrix is in similar fashion to similarity_matrix, rows are mentees, columns are mentors or whatever
for i in range(num_mentors):
    for j in range(num_mentees):
        workload_matrix[i][j] = workload(mentors[i], mentees[j])







        


    

