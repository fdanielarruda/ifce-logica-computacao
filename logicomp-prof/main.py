# from ast import Add

import sys
from formula import *
from functions import *
from semantics import *
from restrictions import *

if(len(sys.argv) >= 3):
    dados = []
    dados_copy = []

    if(int(sys.argv[2]) > 0):
        name_file = sys.argv[1]
        m = sys.argv[2]
    else:
        print("Erro: Você deve fornecer pelo menos a quantidade de uma regra")
        sys.exit()

    try:
        with open(f"{name_file}", 'r') as fp:
            for data in fp:
                dados.append(data.split(','))

        if(not dados):
            print("Erro: Arquivo sem dados.")
            sys.exit()
        else:
            count = 0

        cols_data = []
        pathologies = []
        no_pathologies = []

        [cols_data, pathologies, no_pathologies] = separate_pathologies(dados, [], [], [])
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