from flask import Flask, make_response,render_template,request
import pickle

app = Flask(__name__)

@app.route('/')
def first():
    return render_template("index.html")

@app.route('/submit', methods=['POST']) 
def registration():
    text=request.form.get('hello')
    pickled_tfi=pickle.load(open('prediction_tfi.pkl','rb'))
    pickled_model=pickle.load(open('prediction_model_1.pkl',"rb"))
    test = pickled_tfi.transform([text])
    pred1=pickled_model.predict(test)[0]
    print(pred1)
    return render_template("index.html",pred=pred1)
    

# @app.route('/qr')
# def generate_qr(text):
#     return render_template("index.html")
    

if __name__=='__main__':
     app.run(debug=True)