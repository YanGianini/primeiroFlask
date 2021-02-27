from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cafepuro')
def cafe_puro():
    return render_template('cafepuro.html')

@app.route('/capuccino')
def capuccino():
    return render_template('capuccino.html')

@app.route('/chachai')
def chachai():
    return render_template('chachai.html')

@app.route('/mocaccino')
def mocaccino():
    return render_template('mocaccino.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == "__main__":
    app.run(debug=True)
