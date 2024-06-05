from flask import Flask

app = Flask(__name__)

@app.route('/')
def saluto():
    
        return('ciao')

if __name__ == '__main__':

    app.run(debug=True)