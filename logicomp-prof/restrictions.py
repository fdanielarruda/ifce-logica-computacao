# Para cada atributo e cada regra, temos exatamente uma das trˆes possibilidades: o atributo aparece positivamente na regra, o atributo aparece negativamente na regra ou o atributo n˜ao aparece na regra.
from formula import *
from functions import *

def mounted_atom(atribute, m, letter):
    return Atom("X " + atribute + ", " + str(m) + ", " + letter)

def restriction_01(m, atributes):
    formula = []

    for count_m in range(1, m + 1):
        and_restriction_01 = []

        # (p^~n^~s) V (~p^n^~s) V (~p^~n^s) === (((p^~n)^~s) V ((~p^n)^~s)) V ((~p^~n)^s)
        for atribute in atributes:
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
        cols_formula = and_all(and_restriction_01)
        formula.append(cols_formula)
    
    # A ("azão") com a quantidade de regras apresentadas
    return and_all(formula)

def restriction_02(m, atributes):
    formula = []

    for count_m in range(1, m + 1):
        or_restriction_02 = []

        for atribute in atributes:
            or_restriction_02.append(Not(mounted_atom(atribute, count_m, "s")))

        cols_formula = or_all(or_restriction_02)
        formula.append(cols_formula)

    return and_all(formula)