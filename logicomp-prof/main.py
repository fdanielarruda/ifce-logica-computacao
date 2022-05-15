from formula import *
from functions import *

# Aqui ficará o executável do projeto

loja_aberta = Atom('a loja estava aberta')
funcionarios_atendendo = Atom('os funcionários estavam atendendo')

formula1 = Or(Or(Not(loja_aberta), Not(funcionarios_atendendo)), And(loja_aberta, funcionarios_atendendo))

for atom in atoms(formula1):
    print(atom)