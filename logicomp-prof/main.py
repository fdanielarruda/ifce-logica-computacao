from ast import Add
from formula import *
from functions import *
from semantics import *

# Aqui ficará o executável do projeto

# atomP = Atom('p')
# atomQ = Atom('q')

# formula = (Not(atomP))
# interpretation = {'p': False, 'q': False}

# print(truth_value(formula, interpretation))

atomP = Atom('p')
atomQ = Atom('q')

formula = Or(And((atomP), (atomQ)), (atomQ))
# interpretation = {'p': False, 'q': False}

print(satisfiability_brute_force(formula))