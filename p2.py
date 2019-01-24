from flask import Flask
app = Flask(__name__)

@app.route('/hi/<name>')
def hello_name(name):
    return 'hello ' + name

@app.route('/hi/<int:no>')
def hello_nt(no):
    return 'Roll number %d' % no

@app.route('/hi/<float:fno>')
def hello_fnt(fno):
    return 'number %a' % fno

if __name__=="__main__":
        app.run(debug=True)



