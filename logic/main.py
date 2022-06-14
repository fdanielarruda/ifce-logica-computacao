# from ast import Add

import sys
from formula import *
from functions import *
from semantics import *
from restrictions import *

if(len(sys.argv) >= 3):
    dados = []
    dados_copy = []
    # 

    if(int(sys.argv[2]) > 0):
        name_file = sys.argv[1]
        m = int(sys.argv[2])
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

        # EXECUTÁVEL DO PROJETO
        attributes = []
        pathologies = []
        no_pathologies = []

        [attributes, pathologies, no_pathologies] = separate_pathologies(dados, [], [], [])
        
        print("aguarde...")

        condition_for_algorithm = and_all([
            restriction_01(m, attributes),
            restriction_02(m, attributes),
            restriction_03(m, attributes, no_pathologies),
            restriction_04(m, attributes, pathologies),
            restriction_05(m, pathologies)
        ])
        
        solution_for_problem = satisfiability_brute_force(condition_for_algorithm)
        
        rules(solution_for_problem)

    except IOError:
        print("Erro: Arquivo não acessível")
    finally:
        sys.exit()
else:
    print("Erro: Você deve fornecer os seguinte comando: python main.py nome_arquivo.csv quantidade_regras")
    sys.exit()