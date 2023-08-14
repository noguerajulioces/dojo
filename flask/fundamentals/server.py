from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = 'keep it secret, keep it safe' #CLAVE SECRETA NECESARIA

""""
# tarea chessboard
# @app.route('/')
# def blank_chessboard():
#     return render_template('index.html')

# @app.route('/<int:x>')
# def custom_chessboard(x):
#     return render_template('custom.html', x= x)

#clase sobre listas y diccionarios
@app.route('/lists')
def render_lists():
    students_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = students_info)

#tarea de tabla html
@app.route('/tabla')
def table_html():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("table.html", users = users)

#ENVIO DE FORMULARIO POST
@app.route('/')
def index():
    return render_template("form.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name'] #con estas dos prop ya tenemos acceso a esos datos de post
    session['useremail'] = request.form['email']
    return redirect('/show') #FUNDAMENTAL DIRECCIONAR A LA PAGINA DE ORIGEN

@app.route('/show')
def show_user():
    return render_template('show.html')
"""
@app.route('/', methods=['GET', 'POST'])
def counter():
    if request.method == 'POST':
        session['user_visit'] = int(request.form['user_visit']) + 1
    else:
        session.setdefault('user_visit', 0)  # Inicializar user_visit si no existe en la sesión
    return render_template('counter.html', user_visit=session['user_visit'])

@app.route('/destroy_session', methods=['GET', 'POST'])
def destroy_session():
    session.clear() 
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)