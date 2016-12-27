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
        relations = matrix_relations.find_relations(matrix)
        result = matrix_result.relations_table(relations)
        return render_template('type.html', result=Markup(result))


@app.route("/reflecsive", methods=["GET", "POST"])
def m_reflecsive():
    if request.method == "GET":
        return render_template("closures.html", title="Reflecsive closure")
    elif request.method == "POST":
        matrix = matrix_result.read_matrix(0)
        new_matrix = matrix_closures.reflexive_closure(matrix)
        result = matrix_result.matrix_table(new_matrix)
        return render_template("closures.html", title="Reflecsive closure", result=Markup(result))


@app.route("/symmetric", methods=["GET", "POST"])
def m_symmetric():
    if request.method == "GET":
        return render_template("closures.html", title="Symmetric closure")
    elif request.method == "POST":
        matrix = matrix_result.read_matrix(0)
        new_matrix = matrix_closures.symmetric_closure(matrix)
        result = matrix_result.matrix_table(new_matrix)
        return render_template("closures.html", title="Symmetric closure", result=Markup(result))


@app.route("/transitive", methods=["GET", "POST"])
def m_transitive():
    if request.method == "GET":
        return render_template("closures.html", title="Transitive closure")
    elif request.method == "POST":
        matrix = matrix_result.read_matrix(0)
        new_matrix = matrix_closures.transitive_closure(matrix)
        result = matrix_result.matrix_table(new_matrix)
        return render_template("closures.html", title="Transitive closure", result=Markup(result))


@app.route("/equivalent", methods=["GET", "POST"])
def m_equivalent():
    if request.method == "GET":
        return render_template("closures.html", title="Equivalent closure")
    elif request.method == "POST":
        matrix = matrix_result.read_matrix(0)
        new_matrix = matrix_closures.equivalent_closure(matrix)
        result = matrix_result.matrix_table(new_matrix)
        return render_template("closures.html", title="Equivalent closure", result=Markup(result))


@app.route("/multiplication", methods=["GET", "POST"])
def m_multiplication():
    if request.method == "GET":
        return render_template("multiplication.html")
    elif request.method == "POST":
        matrix1 = matrix_result.read_matrix(1)
        matrix2 = matrix_result.read_matrix(2)
        new_matrix = matrix_multiply.matrix_multiply(matrix1, matrix2)
        result = matrix_result.matrix_table(new_matrix)
        return render_template("multiplication.html", result=Markup(result))


if __name__ == '__main__':
    app.run(debug=True)
