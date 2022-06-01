"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from numpy import True_
from formula import *
from functions import atoms


def truth_value(formula, interpretation):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    
    if isinstance(formula, Atom): # determina se a formula é um atomo e se for retorna a interpretation
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
    interpretation = {}
    return sat(formula, list_atoms, interpretation)

    # ======== YOUR CODE HERE ========
    
def sat(formula, atoms, interpretation):
    
    if atoms == {}:
        if truth_value(formula, interpretation):
            return interpretation
        else:
            return False

    atom = atoms.pop()
    interpretation1 = interpretation.union(atom, True)
    interpretation2 = interpretation.union(atom, False)

    result = sat(formula, atoms, interpretation1)

    if result != False:
        return interpretation1

    return sat(formula, atoms, interpretation2)

