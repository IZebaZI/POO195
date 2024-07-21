from flask import Flask, request, render_template, jsonify, url_for, redirect, flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os
from os import path
from os import remove


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'
app.secret_key = 'your_secret_key'

mysql = MySQL(app)

def listaArchivos():
    urlFiles = 'Vistas/static/docs'
    return (os.listdir(urlFiles))

@app.route('/')
def index():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from albums')
        listaAlbums = cursor.fetchall()
        listaPortadas = listaArchivos()
        return render_template('index.html', albums = listaAlbums, portadas = listaPortadas)
    except Exception as e:
        print(e)

@app.route('/guardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        year = request.form['intYear']
        
        cursor = mysql.connection.cursor()
        cursor.execute('insert into albums(titulo, artista, año) values(%s, %s, %s)', (titulo, artista, year))
        mysql.connection.commit()
        cursor.close()

        cursor = mysql.connection.cursor()
        cursor.execute('select id from albums where titulo=%s and artista=%s and año=%s', (titulo, artista, year))
        id = cursor.fetchone()
        id = str(id[0])
        cursor.close()

        portada = request.files['imgPortada']
        basepath = path.dirname(__file__)
        filename = secure_filename(portada.filename)
        extension = path.splitext(filename)[1]
        nuevoNombre = id + extension
        uploadpath = path.join(basepath, 'static/docs', nuevoNombre)
        portada.save(uploadpath)

        
        flash("Album Guardado Exitosamente")
        return redirect(url_for('index'))

@app.route('/editar/<id>')
def editarAlbum(id):
    cursor = mysql.connection.cursor()
    cursor.execute('select * from albums where id = %s', [id])
    albumEdit = cursor.fetchone()
    listaPortadas = listaArchivos()
    return render_template('edit.html', album = albumEdit, portadas = listaPortadas)

@app.route('/actualizarAlbum/<id>', methods=['POST'])
def actualizarAlbum(id):
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        year = request.form['intYear']
        print(titulo, artista, year)
        
        cursor = mysql.connection.cursor()
        cursor.execute('update albums set titulo=%s, artista=%s, año=%s where id=%s', (titulo, artista, year, id))
        mysql.connection.commit()
        
        portada = request.files['imgPortada']
        if portada.filename != '':
            basepath = path.dirname(__file__)
            filename = secure_filename(portada.filename)
            extension = path.splitext(filename)[1]
            nuevoNombre = id + extension
            uploadpath = path.join(basepath, 'static/docs', nuevoNombre)

            for ext in ['.jpg', '.png']:
                if ext == extension:
                    continue
                fotoAnterior = id + ext
                pathAnterior = path.join(basepath, 'static/docs', fotoAnterior)
                if path.exists(pathAnterior):
                    remove(pathAnterior)

            portada.save(uploadpath)

        flash("Album Editado Exitosamente")
        return redirect(url_for('index'))

@app.route('/eliminar/<id>')
def eliminarAlbum(id):
    cursor = mysql.connection.cursor()
    cursor.execute('delete from albums where id=%s', [id])
    mysql.connection.commit()
    cursor.close()

    for ext in ['.jpg', '.png']:
        fotoAnterior = id + ext
        basepath = path.dirname(__file__)
        pathAnterior = path.join(basepath, 'static/docs', fotoAnterior)
        if path.exists(pathAnterior):
            remove(pathAnterior)
    
    flash("Album Eliminado Exitosamente")
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