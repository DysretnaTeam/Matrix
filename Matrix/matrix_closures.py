# Makes a reflexive, symmetric and transitive closures of matrix
# created: 22.12.2016


def reflexive_closure(matrix):
    '''
    (list(list)) -> list(list)

    Makes reflexive closure of relation shown by matrix
    Returns updated matrix in list of lists

    >>> reflexive_closure([[0,1,1],[0,0,1],[0,0,0]])
    [[1,1,1],[0,1,1],[0,0,1]]
    '''
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            matrix[i][i] = 1

    return matrix


def symmetric_closure(matrix):
    '''
    (list(list)) -> list(list)

    Makes symmetric closure of relation shown by matrix
    Returns updated matrix in list of lists
    >>> symmetric_closure([[0,1,1],[0,1,1],[0,0,1]])
    [[0,1,1],[1,1,1],[1,1,1]]
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix[j][i] != 1:
                matrix[j][i] = 1

    return matrix


def transitive_closure(matrix):
    """
    list(tuple(int)) -> list(tuple(int))

    Makes a transitive closure of matrix.

    >>> transitive_closure([[1, 1, 0], [1, 1, 0], [0, 1, 0]])
    [[1, 1, 0], [1, 1, 0], [1, 1, 0]]
    >>> transitive_closure([[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 0, 0]])
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    >>> transitive_closure([[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
    [[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
    >>> transitive_closure(1011)
    """
    try:
        new_matrix = matrix.copy()
        for row in range(len(new_matrix)):
            for line in range(len(new_matrix)):
                for element in range(len(new_matrix)):
                    new_matrix[line][element] = new_matrix[line][element] or (new_matrix[line][row] and new_matrix[row][element])
        return new_matrix
    except:
        return


def equivalent_closure(matrix):
    '''
    (list(list)) -> (list(list))

    Makes from given relation shown by matrix equivalence relation shown by matrix
    Returns this matrix in list of lists

    >>> equivalent_closure([[1,1],[0,1]])
    [[1,1], [1,1]]
    '''
    import matrix_relations

    i = 0
    while not matrix_relations.is_equivalent(matrix):
        if not matrix_relations.is_reflexive(matrix):
            matrix = reflexive_closure(matrix)
        elif not matrix_relations.is_symmetric(matrix):
            matrix = symmetric_closure(matrix)
        elif not matrix_relations.is_transitive:
            matrix = transitive_closure(matrix)

        if i == 10000:
            return [["Sorry, it's impossible to make relation of equivalence :("]]

        i += 1

    return matrix
