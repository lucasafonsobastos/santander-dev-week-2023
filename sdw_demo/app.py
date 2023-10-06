from flask import Flask, request, render_template
import requests
import json

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

app = Flask(__name__)

def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<id>')
def cliente(id):
    users = get_user(id)
    print(users['account']['number'])
    return render_template(
        'home.html', 
        cliente = users['name'],
        conta = users['account']['number'],
        agencia = users['account']['agency'],
        saldo = users['account']['limit'],
        card = users['card']['number'][-4:],
        mensagens = users['news']
    )

if __name__ == '__main__':
    app.run(debug=True)
