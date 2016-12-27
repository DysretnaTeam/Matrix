# Flask application for Matrix.com
# Templates: home.html, type.html, closures.html, multiplicaion.html
# Static: home.css, jquery.js, my_multiply.js, my_trans.js
# Python modules: matrix_result.py, matrix_relations.py, matrix_closures.py, matrix_multiply.py


from flask import Flask, render_template, request, url_for, redirect, Markup
import matrix_result
import matrix_relations, matrix_closures, matrix_multiply


app = Flask(__name__)


@app.route('/')
def main():
    return redirect(url_for("home"))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/type', methods=["GET", "POST"])
def m_type():
    if request.method == "GET":
        return render_template('type.html')
    elif request.method == "POST":
        matrix = matrix_result.read_matrix(0)
        input_matrix_table = matrix_result.matrix_table(matrix)
        relations = matrix_relations.find_relations(matrix)
        result_relations = matrix_result.relations_table(relations)
        return render_template('type.html', inputed_matrix=Markup(input_matrix_table),
                               result_relations=Markup(result_relations))


@app.route("/reflecsive", methods=["GET", "POST"])
def m_reflecsive():
    if request.method == "GET":
        return render_template("closures.html", title="Reflecsive closure")
    elif request.method == "POST":
        matrix = matrix_result.read_matrix(0)
        input_matrix_table = matrix_result.matrix_table(matrix)
        new_matrix = matrix_closures.reflexive_closure(matrix)
        result_matrix = matrix_result.matrix_table(new_matrix)
        return render_template("closures.html", title="Reflecsive closure",
                               inputed_matrix=Markup(input_matrix_table), result_matrix=Markup(result_matrix))


@app.route("/symmetric", methods=["GET", "POST"])
def m_symmetric():
    if request.method == "GET":
        return render_template("closures.html", title="Symmetric closure")
    elif request.method == "POST":
        matrix = matrix_result.read_matrix(0)
        input_matrix_table = matrix_result.matrix_table(matrix)
        new_matrix = matrix_closures.symmetric_closure(matrix)
        result_matrix = matrix_result.matrix_table(new_matrix)
        return render_template("closures.html", title="Symmetric closure",
                               inputed_matrix=Markup(input_matrix_table), result_matrix=Markup(result_matrix))


@app.route("/transitive", methods=["GET", "POST"])
def m_transitive():
    if request.method == "GET":
        return render_template("closures.html", title="Transitive closure")
    elif request.method == "POST":
        matrix = matrix_result.read_matrix(0)
        input_matrix_table = matrix_result.matrix_table(matrix)
        new_matrix = matrix_closures.transitive_closure(matrix)
        result_matrix = matrix_result.matrix_table(new_matrix)
        return render_template("closures.html", title="Transitive closure",
                               inputed_matrix=Markup(input_matrix_table), result_matrix=Markup(result_matrix))


@app.route("/equivalent", methods=["GET", "POST"])
def m_equivalent():
    if request.method == "GET":
        return render_template("closures.html", title="Equivalent closure")
    elif request.method == "POST":
        matrix = matrix_result.read_matrix(0)
        input_matrix_table = matrix_result.matrix_table(matrix)
        new_matrix = matrix_closures.equivalent_closure(matrix)
        result_matrix = matrix_result.matrix_table(new_matrix)
        return render_template("closures.html", title="Equivalent closure",
                               inputed_matrix=Markup(input_matrix_table), result_matrix=Markup(result_matrix))


@app.route("/multiplication", methods=["GET", "POST"])
def m_multiplication():
    if request.method == "GET":
        return render_template("multiplication.html")
    elif request.method == "POST":
        matrix1 = matrix_result.read_matrix(1)
        matrix2 = matrix_result.read_matrix(2)
        input_matrix_table1 = matrix_result.matrix_table(matrix1)
        input_matrix_table2 = matrix_result.matrix_table(matrix2)
        new_matrix = matrix_multiply.matrix_multiply(matrix1, matrix2)
        result_matrix = matrix_result.matrix_table(new_matrix)
        return render_template("multiplication.html", inputed_matrix1=Markup(input_matrix_table1),
                               inputed_matrix2=Markup(input_matrix_table2), result_matrix=Markup(result_matrix))


if __name__ == '__main__':
    app.run(debug=True)
