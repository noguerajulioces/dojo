from flask import Flask, render_template  # agregado render_template!
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    #return 'Hola fue un exito!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta
    usuario_id= 15
    usuario_name= "Maria"
    usuario_dict= {
        'usuario': usuario_id,
        'usuario_name': usuario_name,
        'age': 38,
        'pasatiempos': ['dormir', 'leer', 'peliculas', 'musicas']
    }
    return render_template('templates/inicial.html', user=usuario_id, name=usuario_name, user_dict=usuario_dict)  #RUTA DEL RENDER

@app.route('/test')
def test():
    return 'hello'


# @app.route('/m/<track>/<unidad>/<pagina>')
# def coding_dojo(track, unidad, pagina):
#     return f"Estas en el track {track} en la unidad {unidad} en la pagina {pagina}"

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración, es decir me da toda la info e lo que pide y retorna, no es necesario


