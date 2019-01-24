from flask import Flask, render_template
app = Flask(__name__)

@app.route("/result")
def result():
   # name = 'abc'
    #list1 = [12,13,15,16]
   # return render_template('tmp.html',name = list1[1]) 

    dict1 = {'Maths':80,'C':70,'Java':80}
    print(dict1)
    return render_template('tmp2.html', result = dict1)

if __name__=="__main__":
        app.run(debug=True)
