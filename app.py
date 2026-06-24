from flask import Flask,render_template,url_for,request
import joblib
model = joblib.load(r"data\rfr1_model.lb")
app =Flask(__name__)

@app.route('/')
def intro():
    return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/history')
def history():
    return render_template('history.html')
@app.route('/about')
def about():
    return render_template('about.html')
'''@app.route('/project')
def predict():
    return render_template('project.html')'''

@app.route('/project',methods = ['GET','POST'])
def predict():
    if request.method=="POST":
        brand_name = request.form['brand_name']
        owner=int(request.form['owner'])
        age=int(request.form['age'])
        power=int(request.form['power'])
        kms_driven=int(request.form['kms_driven'])

        brand_dict = {
         'TVS':1,   'Royal Enfield':2,         'Triumph':3,          'Yamaha':4,
           'Honda':5,            'Hero':6,           'Bajaj':7,          'Suzuki':8,
         'Benelli':9,             'KTM':10,        'Mahindra':11,        'Kawasaki':12,
          'Ducati':13,         'Hyosung':14, 'Harley-Davidson':15,            'Jawa':16,
             'BMW':17,          'Indian':18,         'Rajdoot':19,             'LML':20,
           'Yezdi':21,              'MV':22,           'Ideal':23
        }
        brand_name = brand_dict.get(brand_name)
        data =[[brand_name,age,kms_driven,power,owner]]
        pred =model.predict(data)
        print("Prediction-->",pred)
        #print(type(brand_name),type(owner),type(age),type(kms_driven),type(power))
    
        return render_template('project.html',prediction =pred)
'''@app.route('/home')
def home():
    return "I live in jaipur"'''


if __name__=="__main__":
    app.run(debug =True)