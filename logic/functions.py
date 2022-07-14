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
        return formula

    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            return formula
        else:
            is_negation_normal_form(formula)
    
    if isinstance(formula, Or):
        return (Or(is_negation_normal_form(formula.left), is_negation_normal_form(formula.right)))

    if isinstance(formula, And):
        return (And(is_negation_normal_form(formula.left), is_negation_normal_form(formula.right)))

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

# LISTA 02
def to_cnf(formulas):
    result = remove_implies(formulas)
    result = is_negation_normal_form(result) # Já havia no repositório
    result = distributive(result)

    return result

def remove_implies(formula):
    # a
    if isinstance(formula, Atom):
        return formula

    # ~a
    elif isinstance(formula, Not):
        return (Not(remove_implies(formula.inner)))

    # a ^ b 
    elif isinstance(formula, And):
        return (And(remove_implies(formula.left), remove_implies(formula.right)))

    # a V b 
    elif isinstance(formula, Or):
        return (Or(remove_implies(formula.left), remove_implies(formula.right)))

    # ~a V b
    elif isinstance(formula, Implies):
        return (Or(Not(remove_implies(formula.left)), remove_implies(formula.right)))

def distributive(formula):
    if isinstance(formula, Atom):
        return formula

    if isinstance(formula, And):
        return And(distributive(formula.left), distributive(formula.right))

    if isinstance(formula, Or):
        b1 = distributive(formula.left)
        b2 = distributive(formula.right)

        if isinstance(b1, And):
            return And(distributive(Or(b1.left, b2)), distributive(Or(b1.right, b2)))

        if isinstance(b2, And):
            return And(distributive(Or(b1, b2.left)), distributive(Or(b1, b2.right)))

        return Or(b1, b2)

    return formula

def solution_cnf(formulas):
    atomics = {}
    atomics_list = atoms(formulas)
    count = 1

    # CRIANDO UM ARRAY COM AS ATOMICAS DA FÓRMULA
    for atomic in atomics_list:
        atomics[str(atomic)] = count
        count += 1

    # CONVERTER FÓRMULA
    cnf_list = clause_for_solutions(formulas)

    # CONVERTER ATOMICAS PARA NÚMEROS
    cnf_list = atomic_to_number(cnf_list, atomics)
    
    return [cnf_list, atomics_list]

def clause_for_solutions(formula):
    result = []

    # [1, 2] [3, 4] = (X1 v X2) ^ (X1 V X2) 
    if isinstance(formula, And):
        recursive_clauses_of_list(formula, result)
    else:
        result.append(formula)

    return result

def recursive_clauses_of_list(formula, result):
    if isinstance(formula.left, And):
        recursive_clauses_of_list(formula.left, result)
    else:
        result.append([formula.left])

    if isinstance(formula.right, And):
        recursive_clauses_of_list(formula.right, result)
    else:
        result.append([formula.right])

def atomic_to_number(list, atomics):
    result = []

    for clause in list:
        result.append(run_clauses(clause, atomics))

    return result

def run_clauses(clause, atomics):
    result = []

    for item in clause:
        recursive_clauses_join(item, atomics, result)
    
    return result

def recursive_clauses_join(formula, atomics, result): 
    if isinstance(formula, Atom):
        result.append(atomics[str(formula)])

    elif isinstance(formula, Not):
        result.append(atomics[str(formula.inner)] * -1)
    
    elif isinstance(formula, Or):
        recursive_clauses_join(formula.left, atomics, result)
        recursive_clauses_join(formula.right, atomics, result)

def number_to_atomics(numbers, atomics):
    index = 0
    rules = {}

    for atomic in atomics:
        if numbers[index] > 0:
            rules[str(atomic)] = True
        else:
            rules[str(atomic)] = False
        
        index += 1

    return rules