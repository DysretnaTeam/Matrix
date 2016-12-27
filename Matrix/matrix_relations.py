# Finds all matrix relations
# created: 22.12.2016


def is_reflexive(matrix):
    '''
    list(list(int)) -> str or None

    Checks if the matrix is reflexive

    >>> is_reflexive([[1,0,0],[1,1,0],[0,0,1]])
    'reflexive'
    >>> is_reflexive([[1,0,1,1],[1,1,0,1],[0,1,1,0],[1,0,0,1]])
    'reflexive'
    >>> is_reflexive([[1,0,0],[1,1,0],[1,1,0]])
    '''
    for raw in range(len(matrix)):
        if not matrix[raw][raw]:
            return
    return 'reflexive'


def is_irreflexive(matrix):
    """
    list(list(int)) -> str or None

    Checks if the matrix is symmetric

    >>> is_irreflexive([[0,0,1],[1,0,1],[1,0,0]])
    'irreflexive'
    >>> is_irreflexive([[0,0,1,1],[1,0,0,1],[1,1,0,0],[1,1,1,0]])
    'irreflexive'
    >>> is_irreflexive([[0,0,1],[1,0,1],[1,1,1]])
    """
    for row_column in range(len(matrix) - 1):
        if matrix[row_column][row_column] != matrix[row_column + 1][row_column + 1] or matrix[row_column][row_column]:
            return
    return "irreflexive"


def is_symmetric(matrix):
    """
    list(list(int)) -> str or None

    Checks if the matrix is symmetric

    >>> is_symmetric([[1,0,1],[0,0,1],[1,1,1]])
    'symmetric'
    >>> is_symmetric([[1,1,1,1],[1,0,1,0],[1,1,1,0],[1,0,0,0]])
    'symmetric'
    >>> is_symmetric([[1,0,1,1],[0,0,1,0],[1,0,1,0],[1,1,0,0]])
    """
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] != matrix[column][row] and matrix[row][column] == 1:
                return
    return "symmetric"


def is_antisymmetric(matrix):
    '''
    list(list(int)) -> str or None

    Checks if the matrix is antisymmetric

    >>> is_antisymmetric([[0,1,1],[0,0,0],[0,1,0]])
    'antisymmetric'
    >>> is_antisymmetric([[0,1,1,1],[0,0,0,1],[0,1,0,1],[0,0,0,1]])
    'antisymmetric'
    >>> is_antisymmetric([[0,1,1,1],[1,0,0,1],[0,1,0,1],[0,0,0,1]])
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and (matrix[i][j] and matrix[j][i]):
                return
    return 'antisymmetric'


def is_asymmetric(matrix):
    """
    list(list(int)) -> str or None

    Checks if the matrix is symmetric

    >>> is_asymmetric([[0,1,1],[0,0,0],[0,1,0]])
    'asymmetric'
    >>> is_asymmetric([[0,1,1,1],[0,0,0,1],[0,1,0,1],[0,0,0,0]])
    'asymmetric'
    >>> is_asymmetric([[0,1,0,1],[0,0,0,1],[0,1,1,0],[0,0,0,0]])
    """
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == 1 and matrix[row][column] == matrix[column][row]:
                return
    return "asymmetric"




def is_transitive(matrix):
    '''
    (list(list)) -> str or None

    Matrix is transitive if the matrix is subset of product of this matrix with itself
    Returns whether relation shown by matrix is transitive

    >>> isTransitive([[0,1],[1,0]])
    >>> isTransitive([[1,1],[1,0]])
    transitive
    '''
    from matrix_multiply import matrix_multiply

    matrix_composition = matrix_multiply(matrix, matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix_composition[i][j] != 1:
                return
    return 'transitive'


def is_equivalent(matrix):
    '''
    (list(list)) -> str or None

    Checks if the relation shown by matrix is equivalence relation
    Equivalence relation is reflexive, symmetric and transitive

    >>> is_equivalent([[1,1],[1,1]])
    'equivalence relation'
    >>> is_equivalent([[1,0,1],[1,1,1],[0,1,1]])
    '''
    if is_reflexive(matrix) and is_symmetric(matrix) and is_transitive(matrix):
        return 'equivalence relation'
    return


def is_part_ord(matrix):
    '''
    (list(list)) -> str or None

    Checks if the relation shown by matrix is relation of part order
    Equivalence relation is reflexive, antisymmetric and transitive

    >>> is_part_ord([[1,1],[0,1]])
    'relation of part order'
    >>> is_part_ord([[1,1,1],[1,0,1],[0,1,1]])
    '''
    if is_reflexive(matrix) and is_antisymmetric(matrix) and is_transitive(matrix):
        return 'relation of part order'
    return


def find_relations(matrix):
    """
    list(list(int)) -> list(str)

    Finds all matrix relations

    >>> find_relations([[1,1,0],[0,1,1],[0,0,1]])
    ['reflexive', 'antisymmetric', 'transitive', 'relation of part order']
    >>> find_relations([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])
    ['irreflexive', 'antisymmetric', 'asymmetric']
    """
    relations = ["reflexive", "irreflexive", "symmetric", "antisymmetric", "asymmetric", "transitive","equivalent", "part_ord"]
    result = []
    for relation in relations:
        f_relation = eval("is_" + relation + "(matrix)")
        if f_relation:
            result.append(f_relation)
    if not result:
        return ["Sorry, this matrix has no type"]
    return result
