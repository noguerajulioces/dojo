from flask import Flask, render_template  
app = Flask (__name__)

@app.route('/')
def blank_chessboard():
    return render_template('index.html')

@app.route('/<int:x>')
def custom_chessboard(x):
    return render_template('custom.html', x= x)

if __name__ == "__main__":
    app.run(debug=True)