# from ast import Add

import sys
from formula import *
from functions import *
from semantics import *

if(len(sys.argv) >= 3):
    dados = []

    if(int(sys.argv[2]) > 0):
        name_file = sys.argv[1]
        quantity_rules = sys.argv[2]
    else:
        print("Erro: Você deve fornecer pelo menos a quantidade de uma regra")
        sys.exit()

    try:
        f = open(name_file, "r")
        dados.append(f.read())
        print(dados)
        
    except IOError:
        print("Erro: Arquivo não acessível")
    finally:
        sys.exit()
else:
    print("Erro: Você deve fornecer os seguinte comando: python main.py nome_arquivo.csv quantidade_regras")
    sys.exit()

# 

# Aqui ficará o executável do projeto

# atomP = Atom('p')
# atomQ = Atom('q')

# formula = (Not(atomP))
# interpretation = {'p': False, 'q': False}

# print(truth_value(formula, interpretation))

# atomP = Atom('p')
# atomQ = Atom('q')

# formula = Or(And((atomP), (atomQ)), (atomQ))
# # interpretation = {'p': False, 'q': False}

# print(satisfiability_brute_force(formula))

# 

# dados = []
# dados.append(["PI <= 42.09", "LA <= 39.63", "GS <= 37.89", "P"])
# dados.append([0,1,1,1])
# dados.append([0,0,0,1])
# dados.append([1,1,1,0])
# dados.append([0,0,1,0])

# cols_data = []
# pathologies = []
# no_pathologies = []
# separate_pathologies(dados, cols_data, pathologies, no_pathologies)
# print(cols_data)