from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('../templates/chessboard.html')

#@app.route('/<int:x>')
#def custom_board(x):
#    return render_template('chessboard.html')

#@app.route('/<int:x>/<int:y>')
#def custom_board_xy(x, y):
#    return render_template('chessboard.html')

if __name__ == '__main__':
    app.run(debug=True) 
