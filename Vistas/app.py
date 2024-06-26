from flask import Flask, request, render_template, jsonify, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
app.secret_key = 'your_secret_key'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        year = request.form['intYear']
        print(titulo, artista, year)
        
        cursor = mysql.connection.cursor()
        cursor.execute('insert into albums(titulo, artista, año) values(%s, %s, %s)', (titulo, artista, year))
        mysql.connection.commit()
        
        flash("Album Guardado Exitosamente")
        return redirect(url_for('index'))

@app.errorhandler(404)
def paginaerror(e):
    return 'Revisa tu sintaxis: No encontré la página especificada'

@app.route('/pruebaConexion')
def pruebaConexion():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT 1")
        datos = cursor.fetchone()
        return jsonify({'status':'Conexion exitosa', 'data':datos})
    except Exception as e:
        return jsonify({'status':'Error de Conexión', 'error':str(e)})

if __name__ == '__main__':
    app.run(port=3000, debug=True)