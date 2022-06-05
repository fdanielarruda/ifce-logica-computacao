"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


# from numpy import True_
from formula import *
from functions import *


def truth_value(formula, interpretation):
    """Determines the truth value of a formula in an interpretation.
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    
    if isinstance(formula, Atom): # determina se a formula é um átomo e se for retorna a interpretation
        atomsInterpretation = interpretation.keys()
        for atomI in atomsInterpretation:
            if str(atomI) == str(formula):
                return interpretation[str(atomI)]

    if isinstance(formula, Not): # determina se a formula é uma negação e se for, retorna F
        return not truth_value(formula.inner, interpretation)

    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):

        if isinstance(formula, Implies):
            return not ( truth_value(formula.left, interpretation) and not truth_value(formula.right, interpretation) )
        if isinstance(formula, And): # retorna o resultado da valoração do
            return truth_value(formula.left, interpretation) and truth_value(formula.right, interpretation)
        if isinstance(formula, Or): # retorna o resultado da valoração do or
            return truth_value(formula.left, interpretation) or truth_value(formula.right, interpretation)

    # ======== YOUR CODE HERE ========


def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""

    list_atoms = atoms(formula)
    interpretation = get_interpretation(formula, [], list_atoms)
    return sat(formula, list_atoms, interpretation)

    # ======== YOUR CODE HERE ========
    
def sat(formula, atoms, interpretation):
    if len(atoms) == 0:
        if truth_value(formula, dict(interpretation)):
            return dict(interpretation)
        else:
            return False

    atom = atoms.pop()
    atoms1 = atoms.copy()

    interpretation1 = interpretation.copy()
    interpretation1.append((str(atom), True))

    interpretation2 = interpretation.copy()
    interpretation2.append((str(atom), False))

    # print(formula, atoms1, interpretation1)
    result = sat(formula, atoms1, interpretation1)

    if result != False:
        return dict(interpretation1)

    return sat(formula, atoms1, interpretation2)

def get_interpretation(formula, interpretation, list_atoms, truth_value = True):
    """ Save the truth value in interpretation and remove atoms from the Atoms """

    if isinstance(formula, Atom): # verifica se a formula é uma atômica
        interpretation.append((str(formula), truth_value))
        remove_atoms(formula, list_atoms)
    
    if isinstance(formula, Not): # verifica se a formula é uma possui not
        get_interpretation(formula.inner, interpretation, list_atoms, False)

    if isinstance(formula, And): # verifica se a formula é um and
        get_interpretation(formula.left, interpretation, list_atoms)
        get_interpretation(formula.right, interpretation, list_atoms)
    
    return interpretation