import random #libraries used to generate random string 
import string


def generate_state(leng,symbol0,symbol1):
    #Creates a random string of fixed lenght
    #requires the lenght of the string, and the characters that have to be used to generate the string
    #symbol0 is associated with the low state while symbol1 with the high state
    #the function returns a random generated string
    return ''.join(random.choices(symbol0+symbol1, k=leng)) 

def traduct(string,rule_select,symbol0,symbol1):
    #Traduction function, taking one number and the string to traduct, 
    #it can produce different rules, 
    #in particular rule 30, rule 90 rule 110 and rule 184
    #requires as parameter the string to traduce, and an integer associated with the rule to follow and the symbols which we use
    #as before symbol0 is associated with low state while symbol 1 with high
    #and returns the character which is associated to that string
    #Explanation of the rules:
    #    30: {"...": '0', "..0": '0', ".0.": '0', "000": '0',
    #          ".00": '.', "0..": '.', "0.0": '.', "00.": '.'},
    #    90: {"...": "0", "..0": ".", ".0.": "0", ".00": ".",
    #         "0..": ".", "0.0": "0", "00.": ".", "000": "0"},
    #    110: {"...": '0', "..0": '.', ".0.": '.', ".00": '0',
    #          "0..": '.', "0.0": '.', "00.": '.', "000": '0'},
    #    184: {"...": ".", "..0": "0", ".0.": ".", ".00": ".",
    #          "0..": ".", "0.0": "0", "00.": "0", "000": "0"}
    RULES = {30: {symbol0+symbol0+symbol0: symbol1, symbol0+symbol0+symbol1: symbol1, symbol0+symbol1+symbol0: symbol1, symbol1+symbol1+symbol1: symbol1,
                  symbol0+symbol1+symbol1: symbol0, symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol0, symbol1+symbol1+symbol0: symbol0},

             90: {symbol0+symbol0+symbol0: symbol1, symbol0+symbol0+symbol1: symbol0, symbol0+symbol1+symbol0: symbol1, symbol0+symbol1+symbol1: symbol0,
                  symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol1, symbol1+symbol1+symbol0: symbol0, symbol1+symbol1+symbol1: symbol1},

             110: {symbol0+symbol0+symbol0: symbol1, symbol0+symbol0+symbol1: symbol0, symbol0+symbol1+symbol0: symbol0, symbol0+symbol1+symbol1: symbol1,
                   symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol0, symbol1+symbol1+symbol0: symbol0, symbol1+symbol1+symbol1: symbol1},

             184: {symbol0+symbol0+symbol0: symbol0, symbol0+symbol0+symbol1: symbol1, symbol0+symbol1+symbol0: symbol0, symbol0+symbol1+symbol1: symbol0,
                   symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol1, symbol1+symbol1+symbol0: symbol1, symbol1+symbol1+symbol1: symbol1}
         }
    return RULES[rule_select][string]

def evolve(state,rule_select,symbol0,symbol1):
    #Controls evolution of motus, following the traduction function defined above;
    #requires as parameter the state which has to be evolved, an integer to select the rule and the symbols which we use to describe our cells,
    #the function returns the new state, defined to be both strings
    new_state=traduct(state[-1]+state[0]+state[1],rule_select,symbol0,symbol1)
    for i in range(len(state)-2):
        new_state+=traduct(state[i:i+3],rule_select,symbol0,symbol1)
    new_state=new_state+traduct(state[-2]+state[-1]+state[0],rule_select,symbol0,symbol1)
    return new_state

def simulation(nsteps,string_len=12,rule_select=30,symbol0='.',symbol1='0'):
    #Main simulation controll, 
    #returns a list of the states which have been defined over the process, 
    #requires as parameters the number of iterations which have to be calculated, 
    #the number of the rule which we want to follow and the lenght of the string we want to describe 
    initial_state = generate_state(string_len,symbol0,symbol1)
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state,rule_select,symbol0,symbol1)
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

risultati=simulation(10,12,30,symbol0='.',symbol1='0')
for i in risultati: print(i)
