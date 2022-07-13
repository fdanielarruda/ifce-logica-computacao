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
            to_cnf(restriction_01(m, attributes)),
            to_cnf(restriction_02(m, attributes)),
            to_cnf(restriction_03(m, attributes, no_pathologies)),
            to_cnf(restriction_04(m, attributes, pathologies)),
            to_cnf(restriction_05(m, pathologies))
        ])

        # print(to_cnf(restriction_01(m, attributes)))
        
        # print("CONDIÇÕES DO ALGORITMO: ")
        # print(restriction_01(m, attributes))
        # print("")
        
        solution_for_problem_cnf = solution_cnf(condition_for_algorithm)
        print(solution_for_problem_cnf)
        # print("SOLUÇÕES PARA O PROBLEMA: ")
        
        # if (solution_for_problem_cnf):
        #     rules(solution_for_problem_cnf)
        # else:
        #     print("Nenhuma possível")

    except IOError:
        print("Erro: Arquivo não acessível")
    finally:
        sys.exit()
else:
    print("Erro: Você deve fornecer os seguinte comando: python main.py nome_arquivo.csv quantidade_regras")
    sys.exit()