import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app =  Flask(__name__)

#Ruta raiz
@app.route('/')
def index():
    return 'Hola Mundo, esta es una prueba para la creación de contenedores automaticos. De igual manera se agrego funcionalidad automatica para verificar repositorio'

if __name__ == '__main__':
    app.run(debug=True)