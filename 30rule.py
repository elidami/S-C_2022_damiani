import random #libraries used to generate random string 
import string


def generate_state(lenght,symbol0,symbol1):
    """
This function randomly generates the initial state.


The function requires as input the following PARAMETERS:
lenght: This parameter is the lenght of the generated string, the expected type is integer; 
symbol0: This parameter corresponds to the low state, the expected type is string;
symbol1: This parameter corresponds to the high state, the expected type is string.

The function RETURNS a string made by the two symbols. The number of symbols in the string is equal to the value of the parameter lenght.

EXAMPLE:
generate_states(3,'0','1') returns a random string choosen between following: "000", "001" , "010" , "100" , "011", "101", "110", "111".

    """ 
    return ''.join(random.choices(symbol0+symbol1, k=lenght)) 


def traduct(three_symbols_string,rule_selection,symbol0,symbol1):
    """
This function contains the four possible rules to follow for traducting an input string.

The function requires as input the following PARAMETERS:
three_symbols_string: This parameter is the initial string, the expected type is a string made by symbol0 and/or symbol1 and of lenght equal to three.
rule_selection: This parameter corresponds to the rule to follow, the expected type is one of the following integers: 30, 90, 110, 184. These four rules are defined
	as follows:

		30: {symbol0+symbol0+symbol0: symbol1, symbol0+symbol0+symbol1: symbol1, symbol0+symbol1+symbol0: symbol1, symbol1+symbol1+symbol1: symbol1,
	     	     symbol0+symbol1+symbol1: symbol0, symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol0, symbol1+symbol1+symbol0: symbol0},

		90: {symbol0+symbol0+symbol0: symbol1, symbol0+symbol0+symbol1: symbol0, symbol0+symbol1+symbol0: symbol1, symbol0+symbol1+symbol1: symbol0,
	             symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol1, symbol1+symbol1+symbol0: symbol0, symbol1+symbol1+symbol1: symbol1},

		110: {symbol0+symbol0+symbol0: symbol1, symbol0+symbol0+symbol1: symbol0, symbol0+symbol1+symbol0: symbol0, symbol0+symbol1+symbol1: symbol1,
	     	      symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol0, symbol1+symbol1+symbol0: symbol0, symbol1+symbol1+symbol1: symbol1},

		184: {symbol0+symbol0+symbol0: symbol0, symbol0+symbol0+symbol1: symbol1, symbol0+symbol1+symbol0: symbol0, symbol0+symbol1+symbol1: symbol0,
	              symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol1, symbol1+symbol1+symbol0: symbol1, symbol1+symbol1+symbol1: symbol1}

symbol0:This parameter corresponds to the low state, the expected type is a string;
symbol1:This parameter corresponds to the high state, the expected type is a string.

The function RETURNS a string generated according with the selected rule. 
    """
    RULES = {30: {symbol0+symbol0+symbol0: symbol1, symbol0+symbol0+symbol1: symbol1, symbol0+symbol1+symbol0: symbol1, symbol1+symbol1+symbol1: symbol1,
                  symbol0+symbol1+symbol1: symbol0, symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol0, symbol1+symbol1+symbol0: symbol0},

             90: {symbol0+symbol0+symbol0: symbol1, symbol0+symbol0+symbol1: symbol0, symbol0+symbol1+symbol0: symbol1, symbol0+symbol1+symbol1: symbol0,
                  symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol1, symbol1+symbol1+symbol0: symbol0, symbol1+symbol1+symbol1: symbol1},

             110: {symbol0+symbol0+symbol0: symbol1, symbol0+symbol0+symbol1: symbol0, symbol0+symbol1+symbol0: symbol0, symbol0+symbol1+symbol1: symbol1,
                   symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol0, symbol1+symbol1+symbol0: symbol0, symbol1+symbol1+symbol1: symbol1},

             184: {symbol0+symbol0+symbol0: symbol0, symbol0+symbol0+symbol1: symbol1, symbol0+symbol1+symbol0: symbol0, symbol0+symbol1+symbol1: symbol0,
                   symbol1+symbol0+symbol0: symbol0, symbol1+symbol0+symbol1: symbol1, symbol1+symbol1+symbol0: symbol1, symbol1+symbol1+symbol1: symbol1}
         }

    return RULES[rule_selection][three_symbols_string]

def evolve(state,rule_selection,symbol0,symbol1):
    """
This function is responsible of the evolution of the cellular automata.

The function requires as input the following PARAMETERS:
state: This parameter corresponds to the initial state to evolve, the expected type is a string made by symbol0 and symbol1. 
rule_selection: This parameter corresponds to the rule to follow, the expected type is one of the following integers: 30, 90, 110, 184. The definition of the rules
is contained in the function traduct;
symbol0: This parameter correspond to the low state, the expected type is a string;
symbol1: This parameter correspond to the high state, the expected type is a string.

The function RETURNS a string generated according with the selected rule.

Note: Each symbol of the output string is generated by considering the corresponding symbol in the input string and its two neighbours. The border are treated as
circular; so that, the first symbol of the input string has as neighbours the last symbol and the second symbol of the input string, instead, for the last symbol
of the string the neighbours are the second to last and the first symbols of the input string.

EXAMPLE:
evolve("10111", 30, "0", "1") returns the string "00011", that corresponds to the following sum:
traduct("110", 30, "0", "1") + traduct("101", 30, "0", "1") + traduct( "011", 30, "0", "1") + traduct("111", 30, "0", "1") + traduct("111", 30, "0", "1")

    """

    new_state=traduct(state[-1]+state[0]+state[1],rule_selection,symbol0,symbol1)
    for i in range(len(state)-2):
        new_state+=traduct(state[i:i+3],rule_selection,symbol0,symbol1)
    new_state=new_state+traduct(state[-2]+state[-1]+state[0],rule_selection,symbol0,symbol1)
    return new_state

def simulation(nsteps,string_len=12,rule_select=30,symbol0='.',symbol1='0'):
    """
This function allows to generates consecutive evolutions of the cellular automata. 

Given the lenght of the string and two different symbols, the initial state is randomly generated by using the function generate_state.
Then, the function evolves the system according with the selected rule for a certain number of times.
So that the ith-state is generated by using as input the state i-1 that, in turn, has been generated using the state i-2 and so on. 

The function requires as input the following PARAMETERS:
nsteps: This parameter correspond to the number of evolutions of the cellular automata. The expected type is an integer. 
string_len: This parameter corresponds to the lenght of the initial string and, since during each evolution the lenght is maintained, of all the states of the
simulation. If not specified, the default value for this parameter is 12. 
symbol0:This parameter corresponds to the low state, the expected type is a string, the default value for this parameter is '.'; 
symbol1:This parameter corresponds to the hight state, the expected type is a string, the default value for this parameter is '0'.

The function RETURNS the sequence of consecutive states.

    """ 
    initial_state = generate_state(string_len,symbol0,symbol1)
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state,rule_select,symbol0,symbol1)
        states_seq.append(new_state)
    return states_seq

#TESTING FOR GENERATION
def test_genType():
    assert type(generate_state(12,'_','A')) is str


#TESTING 30RULE
def test_evolve_30_low():
    assert evolve("....",30,'.','0')=="0000"

def test_trad30():
    assert traduct("000",30,".","0")=='0'

def test_evolvelen30():
    assert len(evolve(generate_state(12,'_','A'),30,'_','A'))==len(generate_state(12,'_','A'))


#TESTING 90RULE
def test_evolve_90_low():
    assert evolve("....",90,'.','0')=="0000"

def test_trad90():
    assert traduct("000",90,".","0")=='0'

def test_evolvelen90():
    assert len(evolve(generate_state(12,'_','A'),90,'_','A'))==len(generate_state(12,'_','A'))

#TESTING 110RULE
def test_evolve_110_low():
    assert evolve("....",110,'.','0')=="0000"

def test_trad90():
    assert traduct("000",110,".","0")=='0'

def test_evolvelen110():
    assert len(evolve(generate_state(12,'_','A'),110,'_','A'))==len(generate_state(12,'_','A'))

#TESTING 184RULE
def test_evolve_184_low():
    assert evolve("....",184,'.','0')=="...."

def test_trad184():
    assert traduct("000",184,".","0")=='0'

def test_evolvelen184():
    assert len(evolve(generate_state(12,'_','A'),184,'_','A'))==len(generate_state(12,'_','A'))

