"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


# from numpy import True_
from formula import *
from functions import *

def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""

    atomics = atoms(formula)
    valoration = []

    return sat(formula, atomics, valoration)

def sat(formula, atoms, interpretation):
    if len(atoms) == 0:
        if truth_value(formula, dict(interpretation)):
            return dict(interpretation)
        else:
            return False

    atom = atoms.pop()
    atoms_copy_1 = atoms.copy()
    atoms_copy_2 = atoms.copy()

    interpretation1 = interpretation.copy()
    interpretation1.append((str(atom), True))

    interpretation2 = interpretation.copy()
    interpretation2.append((str(atom), False))

    result = sat(formula, atoms_copy_1, interpretation1)

    if result != False:
        return result

    return sat(formula, atoms_copy_2, interpretation2)
    
def truth_value(formula, interpretation):
    """Determines the truth value of a formula in an interpretation.
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    
    if isinstance(formula, Atom): # se for uma atômica retorna o valor que existe na interpretation
        atomsInterpretation = interpretation.keys()
        for atomI in atomsInterpretation:
            if str(atomI) == str(formula):
                return interpretation[str(atomI)]

    if isinstance(formula, Not): # determina se a formula é uma negação e se for, retorna inverso do valor verdade
        return not truth_value(formula.inner, interpretation)

    if isinstance(formula, Implies): # se for um implica retorna verdadeiro, a menos que sejam V e F, respectivamente
        return not ( truth_value(formula.left, interpretation) and not truth_value(formula.right, interpretation) )

    if isinstance(formula, And): # se for and retorna verdadeiro caso ambos sejam V
        return truth_value(formula.left, interpretation) and truth_value(formula.right, interpretation)

    if isinstance(formula, Or): # se for or retorna verdadeira se um ou outro for v
        return truth_value(formula.left, interpretation) or truth_value(formula.right, interpretation)