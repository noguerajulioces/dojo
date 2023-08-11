from flask import Flask
app = Flask(__name__)

#Localhost:5000/: haz que diga "¡Hola Mundo!"
@app.route('/')
def hola_mundo():
    return 'Hola fue un exito!'

# Localhost:5000/dojo: haz que diga "¡Dojo!"
@app.route('/dojo')
def info_dojo():
    return '¡Dojo!'

#Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos:
# localhost:5000/say/flask: haz que diga "¡Hola, Flask!
@app.route('/say/flask')
def hola_flask():
    return '¡Hola, Flask!'

# localhost:5000/say/ Michael: haz que diga "¡Hola, Michael!"
@app.route('/say/Michael')
def hola_michael():
    return '¡Hola, Michael!'

# localhost:5000/say/john: haz que diga "¡Hola, John!"
@app.route('/say/john')
def hola_john():
    return '¡Hola, John!'

#Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos (PISTA: int() puede ser útil Por ejemplo, int("35") devuelve 35):
# localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
# localhost:5000/repeat/80/bye: haz que diga "adiós" 80 veces
# localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return f"{word} " * num
#aca le pongo http://localhost:5000/repeat/35/hello
if __name__=="__main__": 
    app.run(debug=True)
