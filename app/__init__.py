#importar flask
from flask import Flask, render_template, request, flash
from requests import get
from json import loads

#configurar la app
app = Flask(__name__)

#configurar rutas
@app.route('/hola')
def saludo():
    return  'hola parce'

@app.route('/search', methods=['GET', 'POST'])
def paises():
    print(request.method)
    #definir lista de paises
    if request.method == 'POST':
        try:
            personajes = loads(get(f'https://rickandmortyapi.com/api/character/?name={request.form["name"]}').text)['results']
            return render_template('mm.html', personajes=personajes)
        except:
            return render_template('404.html')
    else:
        return render_template('search.html')


@app.route('/')
def home():
    personajes = loads(get('https://rickandmortyapi.com/api/character').text)
    return render_template('index.html', personajes = personajes['results'])

if __name__ == '__main__':
    app.run()