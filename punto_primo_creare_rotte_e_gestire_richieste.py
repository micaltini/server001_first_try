from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def pagina_iniziale():

    return('questa è la home page')

@app.route('/seconda-pagina')
def secondo_benvenuto():
    return('Ti do il benvenuto sulla seconda pagina')


@app.route('/contatto', methods=['GET', 'POST'])
def f_contatto():

     if request.method == 'POST':
        nome = request.form.get('nome')
        messaggio = request.form.get('messaggio')
        return f'Grazie {nome}! Aggiungerò il tuo messaggio alla lista delle cose di cui non me ne frega un cazzo. \nSto scrivendo tutto sulla mia macchina da scrivere invisibile: {messaggio}'
    

     return'''

        <form method="post" action="/contatto">
            Nome: <input type="text" name="nome"><br>
            Messaggio: <textarea name="messaggio"></textarea><br>
            <input type="submit" value="Invia">
        </form>
          '''






if __name__ == '__main__':

    app.run(debug = True)