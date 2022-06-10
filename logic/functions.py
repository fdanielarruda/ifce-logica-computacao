"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """

from formula import *

def length(formula):
    """Determines the length of a formula in propositional logic."""
    
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1

def subformulas(formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """

    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).

def atoms(formula):
    """Returns the set of all atoms occurring in a formula."""
    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return atoms(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return atoms(formula.left).union(atoms(formula.right))

def number_of_atoms(formula):
    """Returns the number of atoms occurring in a formula."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return number_of_atoms(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_atoms(formula.left) + (number_of_atoms(formula.right))

def number_of_connectives(formula):
    """Returns the number of connectives occurring in a formula."""
    if isinstance(formula, Atom):
        return 0
    if isinstance(formula, Not):
        return number_of_connectives(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_connectives(formula.left) + number_of_connectives(formula.right) + 1

def is_negation_normal_form(formula):
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""

    """ Preciso verificar se a negação só é aplicada apenas nas atómicas e os únicos outros operadores booleanos permitidos são a conjunção ( E ) e disjunção ( OU )."""
            
    if isinstance(formula, Atom):
        return True
    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            return True
        else:
            return False
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        if isinstance(formula, Implies):
            return False
        else:
            if is_negation_normal_form(formula.left) == True and is_negation_normal_form(formula.right) == True:
                return True
            else:
                return False

def separate_pathologies(archive_data, attributes, pathologies, no_pathologies):
    count_data = 0

    for data in archive_data:
        data_new = [] 

        for dado in data: # remove break line
            data_new.append(dado.replace("\n", ""))
        
        data = data_new
        
        if(count_data == 0):
            for col in data:
                if(len(attributes) < len(data) - 1):
                    attributes.append(col)
        else:
            if(int(data[len(data) - 1]) == 0):
                no_pathologies.append(data)
            if(int(data[len(data) - 1]) == 1):
                pathologies.append(data)
        
        count_data += 1
    
    return [attributes, pathologies, no_pathologies]

def and_all(formula):
    count = 0

    for form in formula:
        if (count == 0):
            andall = form
        else:
            andall = And(andall, form)

        count += 1

    return andall

def or_all(formula):
    count = 0

    for form in formula:
        if (count == 0):
            orall = form
        else:
            orall = Or(orall, form)

        count += 1

    return orall

def rules(solution_for_problem):
    rules = {}
    solution_split = ""
    
    for solution in solution_for_problem:
        l = list(solution)
        l[1] = ","
        solution_copy = "".join(l)
        solution_split = solution_copy.split(",")

        if(solution_for_problem[solution]):
            if(solution_split[0] != "C"):
                if(solution_split[2] not in rules):
                    rules[solution_split[2]] = []
                if(solution_split[3] == 'n'):
                    part_split = solution_split[1].split(" ")
                    rules[solution_split[2]].append(part_split[0] + " > " + part_split[2])
                elif(solution_split[3] == 'p'):
                    rules[solution_split[2]].append(solution_split[1])

    all_rules = "{"

    for i, rule in enumerate(rules, start = 0):
        if(i != 0):
            all_rules += ", "
        all_rules += "["

        for index, r in enumerate(rules[rule], start = 0):
            if(index != 0):
                all_rules += ", "
            all_rules += r

        all_rules += "] => P"

    all_rules += "}"

    print(all_rules)
