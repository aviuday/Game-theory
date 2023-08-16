import sys

from GT_data import *


def similarity(mentor, mentee):

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

    cpi_similarity = 1 - abs(class1 - class2)/6

    diff_similarity = 0

    if mentor.diff['Depression'] and mentee.diff['Depression']: 
        diff_similarity += 1
    if mentor.diff['DAC'] and mentee.diff['DAC']: 
        diff_similarity += 1
    if mentor.diff['S_Anxiety'] and mentee.diff['S_Anxiety']: 
        diff_similarity += 1
    if mentor.diff['DX/FR'] and mentee.diff['DX/FR']: 
        diff_similarity += 1

    if not mentor.diff['Depression'] and not mentee.diff['Depression']: 
        diff_similarity += 0.25
    if not mentor.diff['DAC'] and not mentee.diff['DAC']: 
        diff_similarity += 0.25
    if not mentor.diff['S_Anxiety'] and not mentee.diff['S_Anxiety']: 
        diff_similarity += 0.25
    if not mentor.diff['DX/FR'] and not mentee.diff['DX/FR']: 
        diff_similarity += 0.25

    diff_similarity = int(mentee.diff['Depression'])
    
    diff_similarity /= 4 

    interest_similarity = 0

    if mentor.interest['Sports'] and mentee.interest['Sports']: 
        interest_similarity += 1
    if mentor.interest['Cult'] and mentee.interest['Cult']: 
        interest_similarity += 1
    if mentor.interest['Tech'] and mentee.interest['Tech']: 
        interest_similarity += 1
    if mentor.interest['Acads'] and mentee.interest['Acads']: 
        interest_similarity += 1

    if not mentor.interest['Sports'] and not mentee.interest['Sports']: 
        interest_similarity += 0.25
    if not mentor.interest['Cult'] and not mentee.interest['Cult']: 
        interest_similarity += 0.25
    if not mentor.interest['Tech'] and not mentee.interest['Tech']: 
        interest_similarity += 0.25
    if not mentor.interest['Acads'] and not mentee.interest['Acads']: 
        interest_similarity += 0.25
    
    interest_similarity /= 4 

    language_similarity = 0

    for i in range(10):
        if mentor.lang[i] == 1 and mentee.lang[i] == 1:
            language_similarity += 1

    if language_similarity == 0:
        return 0.0
    
    else:
        return (0.33 * cpi_similarity + 0.47 * diff_similarity + 0.20 * interest_similarity)



similarity_matrix = [[0]*num_mentors for i in range(num_mentees)]

for i in range(num_mentees):
    for j in range(num_mentors):
        similarity_matrix[i][j] = similarity(mentees[i], mentors[j])




        


    

