from flask import Flask, render_template  
app = Flask (__name__)

# tarea chessboard
@app.route('/')
def blank_chessboard():
    return render_template('index.html')

@app.route('/<int:x>')
def custom_chessboard(x):
    return render_template('custom.html', x= x)

# tarea de listas
@app.route('/lists')
def render_lists():
    students_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = students_info)

if __name__ == "__main__":
    app.run(debug=True)