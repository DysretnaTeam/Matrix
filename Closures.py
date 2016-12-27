# Makes a reflexive, symmetric and transitive closures of matrix
# authors: Vasyl Borsuk, Ivan Kosarevych
# created: 22.12.2016


def Reflexive_closure(matrix):
    '''
    (list(list)) -> list(list)
    
    Makes reflexive closure of relation shown by matrix
    Returns updated matrix in list of lists
    
    >>> Reflexive_closure([[0,1,1],[0,0,1],[0,0,0]])
    [[1,1,1],[0,1,1],[0,0,1]]
    '''
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            matrix[i][i] = 1
            
    return matrix


def Symmetric_closure(matrix):
    '''
    (list(list)) -> list(list)
    
    Makes symmetric closure of relation shown by matrix
    Returns updated matrix in list of lists

    >>> Symmetric_closure([[0,1,1],[0,1,1],[0,0,1]])
    [[0,1,1],[1,1,1],[1,1,1]]
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix[j][i] != 1:
                matrix[j][i] = 1
                
    return matrix


def Transitive_closure(matrix):
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
