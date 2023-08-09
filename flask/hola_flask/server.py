from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/success')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola fue un exito!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/m/<track>/<unidad>/<pagina>')
def coding_dojo(track, unidad, pagina):
    return f"Estas en el track {track} en la unidad {unidad} en la pagina {pagina}"

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración, es decir me da toda la info e lo que pide y retorna, no es necesario


