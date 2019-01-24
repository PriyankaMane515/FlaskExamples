from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_admin():
   # name = 'abc'
    list1 = [12,13,15,16]
    return render_template('tmp.html',name = list1[1]) 

if __name__=="__main__":
        app.run(debug=True)
