import random #librerie usate per generare una stringa casuale 
import string


def generate_state(leng):
    return ''.join(random.choices('0'+'.', k=leng)) #Creates a random string of fixed lenght 

def traduct(string):
    #Traduction function, taking one number and the string to traduct, 
    #it can produce different rules, 
    #in particular rule 30, rule 90 rule 110 and rule 184
    rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }
    return rule30[string]

def evolve(state):
    new_state=traduct(state[-1]+state[0]+state[1])
    for i in range(len(state)-2):
        new_state+=traduct(state[i:i+3])
    new_state=new_state+traduct(state[-2]+state[-1]+state[0])
    return new_state

def simulation(nsteps,n):
    initial_state = generate_state(12)
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

def test_evolve0():
    assert evolve("0000")=="...."
    
def test_genType():
    assert type(generate_state(12)) is str

def test_trad():
    assert traduct("000")=='.'

def test_evolvelen():
    assert len(evolve(generate_state(12)))==len(generate_state(12))

risultati=simulation(10)
for i in risultati: print(i)
