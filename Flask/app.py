from flask import Flask, request

app = Flask(__name__)

# Ruta Simple
@app.route('/')
def principal():
    return 'Hola Mundo Flask'

# Ruta Doble
@app.route('/usuario')
@app.route('/saludar')
def saludos():
    return 'Hola Sebastián Ramírez'

# Ruta con Parámetros
@app.route('/hi/<nombre>')
def nombre(nombre):
    return '¡Hola '+nombre+'!'

# Definición de Métodos de Trabajo
@app.route('/formulario/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'GET':
        return 'No es seguro utilizar GET'
    elif request.method == 'POST':
        return 'POST es seguro'

# Manejo de Excepciones
@app.errorhandler(404)
def paginaerror(e):
    return 'Revisa tu sintaxis: No encontré la página especificada'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)