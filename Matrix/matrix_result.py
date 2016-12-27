from flask import request


def read_matrix(box):
    """
    int -> list(list(int))

    Reads matrix from html form with checkboxes
    """
    matrix = []
    size = int(request.form.get("size"))
    for line in range(size):
        line_lst = []
        for column in range(size):
            if box:
                name = '(' + str(box) + ',' + str(line) + ',' + str(column) + ')'
            else:
                name = '(' + str(line) + ',' + str(column) + ')'
            state = request.form.get(name)
            if state == 'on':
                line_lst.append(1)
            else:
                line_lst.append(0)
        matrix.append(line_lst)
    return matrix


def relations_table(relations):
    """
    list(str) -> str
    """
    result = "<table id='relation_result'>"
    for relation in relations:
        result += "<tr><td>" + relation + "</td></tr>"
    result += "</table>"
    return result


def matrix_table(matrix):
    """
    list(list(int)) -> str
    """
    result ="<table id='matrix_result'>"
    for line in range(len(matrix)):
        result += "<tr>"
        for column in range(len(matrix)):
            result += "<td>" + str(matrix[line][column]) + "</td>"
        result += "</tr>"
    result += "</table>"
    return result
