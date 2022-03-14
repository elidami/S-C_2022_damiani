def generate_state():
    return ".00."


def traduct(string):
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
    new_state=new_state+traduct(state[-2]+state[-1]+state[1])
    return new_state

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

def test_evolve0():
    assert evolve("0000")=="...."
    
def test_genType():
    assert type(generate_state()) is str

def test_trad():
    assert traduct("000")=='.'

def test_evolvelen():
    assert len(evolve(generate_state()))==len(generate_state())

risultati=simulation(10)
for i in risultati: print(i+"ciao")