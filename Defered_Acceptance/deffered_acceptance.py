# Implementing the deferred acceptance algorithm

from collections import defaultdict

def mentee_without_match(matches, mentees):
    for mentee in mentees:
        if mentee not in matches:
            return mentee


def deferred_acceptance(mentee_prefs, mentor_prefs):
    mentor_queue = defaultdict(int)

    mentees = list(mentee_prefs.keys())

    matches = {}

    while True:
        mentee = mentee_without_match(matches, mentees)
        if not mentee:
            break

        mentor_index = mentor_queue[mentee]
        mentor_queue[mentee] += 1

        try:
            mentor = mentee_prefs[mentee][mentor_index]
        except IndexError:
            matches[mentee] = mentee
            continue

        # print('Trying %s with %s... ' % (mentee, mentor), end='')

        prev_mentee = matches.get(mentor, None)

        if not prev_mentee:
            matches[mentee] = mentor
            matches[mentor] = mentee

            # print('auto')
        elif mentor_prefs[mentor].index(mentee) < \
             mentor_prefs[mentor].index(prev_mentee):
            matches[mentee] = mentor
            matches[mentor] = mentee

            del matches[prev_mentee]

            # print('matched')
        # else:
        #     # print('rejected')

    return {mentee: matches[mentee] for mentee in mentee_prefs.keys()}


# def test_popularity_contest():
#     """Every mentee has the same preferences as every other mentee; same for mentors."""
#     MENTORS = ['M1', 'M2', 'M3']
#     MENTEES = ['m1', 'm2', 'm3', 'm4', 'm5']

#     MENTEE_PREFS = {key: MENTORS.copy() for key in MENTEES}
#     MENTOR_PREFS = {key: MENTEES.copy() for key in MENTORS}

#     print(MENTEE_PREFS)

#     matches = deferred_acceptance(MENTEE_PREFS, MENTOR_PREFS)

#     print(matches)

#     assert matches == {'m1': 'M1', 'm2': 'M2', 'm3': 'M3', 'm4': 'm4', 'm5': 'm5'}


# def test_cycle():
#     """mentees have different preferences, while mentors have identical preferences."""
#     MENTEE_PREFS = {
#         'm1': ['M2'],
#         'm2': ['M1'],
#     }

#     MENTOR_PREFS = {
#         'M1': ['m1'],
#         'M2': ['m2'],
#     }

#     matches = deferred_acceptance(MENTEE_PREFS, MENTOR_PREFS)

#     assert matches == {'m1': 'M2', 'm2': 'M1'}

