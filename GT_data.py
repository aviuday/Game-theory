import numpy as np

np.random.seed(0)

class Student: #Mentor/Mentee
    def __init__(self): #characteristics
        self.mu, self.sigma = 7, 0.5
        self.CPI = np.random.normal(self.mu, self.sigma)
        self.diff = {'Depression': False, 'DAC': False, 'S_Anxiety': False, 'DX/FR': False}
        self.interest = {'Sports': False, 'Cult': False, 'Tech': False, 'Acads': False}
        self.lang = [0] * 10 #E, H, Tel, Tam, Mal, Bel, Punj, NE1, NE2, Guj
        self.update_lang()
        self.update_diff()
        self.update_interests()

    def update_interests(self):
        t = np.random.uniform(0.0, 1.0) #sports: 54% CULT: Acads: Tech
        if(t < 0.55): self.interest['Sports'] = True
        t = np.random.uniform(0.0, 1.0) #sports: 54% CULT: Acads: Tech
        if(t < 0.20): self.interest['Acads'] = True
        t = np.random.uniform(0.0, 1.0) #sports: 54% CULT: Acads: Tech
        if(t < 0.33): self.interest['Cult'] = True
        t = np.random.uniform(0.0, 1.0) #sports: 54% CULT: Acads: Tech
        if(t < 0.19): self.interest['Tech'] = True

    def update_diff(self):
        t = np.random.uniform(0.0, 1.0) #Depression: 0-0.36, DAC: 0-0.05, Social Anxiety: 64%, DX/FR: 0-0.1
        if(t < 0.36): self.diff['Depression'] = True
        t = np.random.uniform(0.0, 1.0) #Depression: 0-0.36, DAC: 0-0.05, Social Anxiety: 64%, DX/FR: 0-0.1
        if(t < 0.60): self.diff['S_Anxiety'] = True
        t = np.random.uniform(0.0, 1.0) #Depression: 0-0.36, DAC: 0-0.05, Social Anxiety: 64%, DX/FR: 0-0.1
        if(t < 0.1): self.diff['DX/FR'] = True
        t = np.random.uniform(0.0, 1.0) #Depression: 0-0.36, DAC: 0-0.05, Social Anxiety: 64%, DX/FR: 0-0.1
        if(t < 0.05): self.diff['DAC'] = True

    def update_lang(self):
        #E:, H, Tel, Tam, Mal, Bel, Punj, NE1, NE2, Guj
        t = np.random.uniform(0.0, 1.0) #Languages
        if(t < 0.9): self.lang[0] = 1 #ENG
        t = np.random.uniform(0.0, 1.0) 
        if(t < 0.75): self.lang[1] = 1 #HIN
        t = np.random.uniform(0.0, 1.0) 
        if(t < 0.20): self.lang[2] = 1 #TEL
        t = np.random.uniform(0.0, 1.0) 
        if(t < 0.06): self.lang[3] = 1 #TAM
        t = np.random.uniform(0.0, 1.0) 
        if(t < 0.15): self.lang[4] = 1 #MAL
        t = np.random.uniform(0.0, 1.0) 
        if(t < 0.04): self.lang[5] = 1 #BEL
        t = np.random.uniform(0.0, 1.0) 
        if(t < 0.02): self.lang[6] = 1 #PUNJ
        t = np.random.uniform(0.0, 1.0) 
        if(t < 0.005): self.lang[7] = 1 #NE1
        t = np.random.uniform(0.0, 1.0) 
        if(t < 0.005): self.lang[8] = 1 #NE2
        t = np.random.uniform(0.0, 1.0) 
        if(t < 0.02): self.lang[9] = 1 #Guj

#50 mentees, 10 mentors
def give_data(no_mentors, no_mentees):
    data = []
    for _ in range(no_mentees + no_mentors):
        student = Student()
        data.append(student)
    mentors = data[:no_mentors]
    mentees = data[no_mentors:]
    assert len(mentors) == no_mentors and len(mentees) == no_mentees
    return mentors, mentees
#(50,500),(100,500),(10,100),(70,490),(80,640)
num_mentors = 80
num_mentees = 640
mentors, mentees = give_data(num_mentors, num_mentees)






