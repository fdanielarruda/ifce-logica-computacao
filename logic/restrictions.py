# Para cada atributo e cada regra, temos exatamente uma das trˆes possibilidades: o atributo aparece positivamente na regra, o atributo aparece negativamente na regra ou o atributo n˜ao aparece na regra.
from formula import *
from functions import *

def mounted_atom(atribute, m, letter):
    return Atom("X " + atribute + "," + str(m) + "," + letter)

def restriction_01(m, attributes):
    formula = []

    for count_m in range(1, m + 1):
        and_restriction_01 = []

        # (p^~n^~s) V (~p^n^~s) V (~p^~n^s) === (((p^~n)^~s) V ((~p^n)^~s)) V ((~p^~n)^s)
        for atribute in attributes:
            and_restriction_01.append(
                Or(
                    Or(
                        And(
                            And(
                                mounted_atom(atribute, count_m, "p"),
                                Not(mounted_atom(atribute, count_m, "n"))
                            ),
                            Not(mounted_atom(atribute, count_m, "s"))
                        ),
                        And(
                            And(
                                Not(mounted_atom(atribute, count_m, "p")),
                                mounted_atom(atribute, count_m, "n")
                            ),
                            Not(mounted_atom(atribute, count_m, "s"))
                        )
                    ),
                    And(
                        And(
                            Not(mounted_atom(atribute, count_m, "p")),
                            Not(mounted_atom(atribute, count_m, "n"))
                        ),
                        mounted_atom(atribute, count_m, "s")
                    )
                )
            )
        
        # A ("azão") com todas as colunas da regra
        formula.append(and_all(and_restriction_01))
    
    # A ("azão") com a quantidade de regras apresentadas
    return and_all(formula)

#Cada regra deve ter algum atributo aparecendo nela.
def restriction_02(m, attributes):
    formula = []

    for count_m in range(1, m + 1):
        or_restriction_02 = []

        for atribute in attributes:
            or_restriction_02.append(Not(mounted_atom(atribute, count_m, "s")))

        formula.append(or_all(or_restriction_02))

    return and_all(formula)

# Para cada paciente sem patologia e cada regra, algum atributo do paciente n˜ao pode ser aplicado à regra
def restriction_03(m, attributes, no_pathologies):
    and_no_pathologie = []

    for no_pathologies_row in no_pathologies:
        formula = []

        for count_m in range(1, m + 1):
            or_restriction_03 = []

            for count_a in range(0, len(attributes)):
                if (int(no_pathologies_row[count_a]) == 1):
                    or_restriction_03.append(mounted_atom(attributes[count_a], count_m, "n"))
                else:
                    or_restriction_03.append(mounted_atom(attributes[count_a], count_m, "p"))

            formula.append(or_all(or_restriction_03))

        and_no_pathologie.append(and_all(formula))
    
    return and_all(and_no_pathologie)

# Para cada paciente com patologia, cada regra e cada atributo, se o atributo do paciente n˜ao se aplicar ao da regra, ent˜ao a regra n˜ao cobre esse paciente.
def restriction_04(m, attributes, pathologies):
    and_pathologies = []

    for count_m in range(1, m + 1):
        formula = []

        for count_p in range(1, len(pathologies) + 1):
            and_restriction_04 = []

            for count_a in range(0, len(attributes)):
                c_not = Not(Atom("C " + str(count_m) + "," + str(count_p)))

                if (int(pathologies[count_p - 1][count_a]) == 0):
                    and_restriction_04.append(Implies(mounted_atom(attributes[count_a], count_m, "p"), c_not))
                else:
                    and_restriction_04.append(Implies(mounted_atom(attributes[count_a], count_m, "n"), c_not))
     
            formula.append(and_all(and_restriction_04))

        and_pathologies.append(and_all(formula))

    return and_all(and_pathologies)

# Cada paciente com patologia deve ser coberto por alguma das regras.
def restriction_05(m, pathologies):
    and_restriction_05 = []

    for count_p in range(1, len(pathologies) + 1):
        or_restriction_05 = []

        for count_m in range(1, m + 1):
            or_restriction_05.append(Atom("C " + str(count_m) + "," + str(count_p)))

        and_restriction_05.append(or_all(or_restriction_05))

    return and_all(and_restriction_05)