import random #librerie usate per generare una stringa casuale 
import string


def generate_state(leng):
    #Creates a random string of fixed lenght
    #requires the lenght of the string e returns a random generated string
    return ''.join(random.choices('0'+'.', k=leng)) 

def traduct(string,rule_select):
    #Traduction function, taking one number and the string to traduct, 
    #it can produce different rules, 
    #in particular rule 30, rule 90 rule 110 and rule 184
    #requires as parameter the string to traduce, and an integer associated with the rule to follow
    #and returns the character which is associated to that string
    RULES = {30: {"...": '0', "..0": '0', ".0.": '0', "000": '0',
              ".00": '.', "0..": '.', "0.0": '.', "00.": '.'},

         90: {"...": "0", "..0": ".", ".0.": "0", ".00": ".",
              "0..": ".", "0.0": "0", "00.": ".", "000": "0"},

         110: {"...": '0', "..0": '.', ".0.": '.', ".00": '0',
               "0..": '.', "0.0": '.', "00.": '.', "000": '0'},

         184: {"...": ".", "..0": "0", ".0.": ".", ".00": ".",
               "0..": ".", "0.0": "0", "00.": "0", "000": "0"}
         }
    return RULES[rule_select][string]

def evolve(state,rule_select):
    #Controls evolution of motus, following the traduction function defined above;
    #require as parameter the state which has to be evolved and an integer to select the rule,
    #and returns the new state, defined to be both strings
    new_state=traduct(state[-1]+state[0]+state[1],rule_select)
    for i in range(len(state)-2):
        new_state+=traduct(state[i:i+3],rule_select)
    new_state=new_state+traduct(state[-2]+state[-1]+state[0],rule_select)
    return new_state

def simulation(nsteps,string_len=12,rule_select=30):
    #Main simulation controll, 
    #returns a list of the states which have been defined over the process, 
    #requires as parameters the number of iterations which have to be calculated, 
    #the number of the rule which we want to follow and the lenght of the string we want to describe 
    initial_state = generate_state(string_len)
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state,rule_select)
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

risultati=simulation(10,12,30)
for i in risultati: print(i)
