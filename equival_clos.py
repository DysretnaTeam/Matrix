# Makes equivalence relation
# authors: Ivan Kosarevych
# created: 24.12.2016

import Closures, matrix_relations


def equiv_rel_clos(matrix):
    '''
    (list(list)) -> (list(list))
    
    Makes from given relation shown by matrix equivalence relation shown by matrix
    Returns this matrix in list of lists
    
    >>> equiv_rel_clos([[1,1],[0,1]])
    [[1,1], [1,1]]
    '''
    while not matrix_relations.is_equiv_rel(matrix):
        if not matrix_relations.is_reflexive(matrix):
            matrix = Closures.Reflexive_closure(matrix)
        elif not matrix_relations.is_symmetric(matrix):
            matrix = Closures.Symmetric_closure(matrix)
        elif not matrix_relations.is_transitive:
            matrix = Closures.Transitive_closure(matrix)
            
    return matrix
