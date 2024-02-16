from flask import Flask,render_template
FAI = Flask(__name__)

@FAI.route('/hello')
def hello():
    return render_template('hello.html')

@FAI.route('/hi')
def hi():
    return render_template('hi.html')

if __name__ == '__main__':
    FAI.run(debug=True)