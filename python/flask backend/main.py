from flask import Flask


def make_bold(func):
    def wrapper():
        return f'<b>{func()}<b>'
    return wrapper


app = Flask(__name__)
@app.route('/')
def hello_world():
    return (f'<h1>hello anyone<h1>'
            f'<p style="text-align:center">this is a pargraph<p>'
            f'<img src="https://media.tenor.co/4Eh1DKj7IcoAAAAc/kitten-duck.gif">')

@app.route('/name/<name>')
def hello_name(name):
    return f'hello {name}'

@app.route('/bye')
@make_bold
def bye():
    return 'bye'

if __name__ =="__main__":
    app.run(debug=True)