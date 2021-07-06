from flask import Flask,redirect,request,render_template,url_for
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('boost.pkl','rb'))

@app.route('/eda')
def eda():
    return render_template('eda1.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        ram=request.form['RAM_GB']
        if ram == '8':
            
            ram=8
        elif ram=='16':
            
            ram=16
        elif ram == '4' :
            ram =4
        else:
            ram=32
        
        ddr=request.form['DDR_Version']
        if ddr== "4":
            ddr=4
        else:
            ddr=3
            
            
        pn=request.form['Processor Name']
        if pn == 'Intel':
            pn=0
        elif pn == 'AMD':
            pn=1
        else:
            pn=2
        
        pt=request.form['Processor Type']
        if pt == 'i5':
            pt=0
        elif pt == 'Ryzen 5':
            pt=1
        elif pt == 'i7':
            pt=2
        elif pt=='i3':
            pt=3
        elif pt == 'Ryzen 7':
            pt = 4
        elif pt == 'Ryzen 3':
            pt=5 
        elif pt == 'SQ1':
            pt=6
        elif pt == 'APU':
            pt=7
        elif pt == 'Pentium':
            pt=8
        elif pt == 'm3':
            pt=9
        elif pt=='i9':
            pt=10
        else:
            pt=11
        os=request.form['Operating System Type']
        if os == 'Windows':
            os=0
        elif os=='Mac':
            os=1
        elif os=='DOS':
            os=2
        else:
            os=3
        s=request.form['Storage_GB']
        if s=='512':
            s=0
        elif s=='1000+256':
            s=1
        elif s== '1000':
            s=2
        elif s=='256':
            s=3
        elif s == '1000+128':
            s=4
        elif s == '128':
            s=5
        elif s == '1000+512':
            s=6
        elif s == '2000':
            s=7
        else:
            s=8
        d=request.form['Disk Drive']
        if d == 'SSD':
            d=0
        elif d == 'Both':
             d=1
        else:
             d=2
        si=float(request.form['Size(Inches)'])   
        c=request.form['Company']
        if c == 'HP':
            c=0
        elif c == 'Asus':
            c=1
        elif c == 'Acer':
            c=2
        elif c == 'Dell':
            c=3
        elif c == 'Lenovo':
            c=4
        elif c == 'MSI':
            c=5
        elif c == 'Apple':
            c=6
        elif c == 'Microsoft':
            c=7
        elif c == 'Avita':
            c=8
        elif c == 'Alienware':
            c=9
        else:
            c=10
        gc=request.form['Graphic Card']
        if gc == 'yes':
            gc=1
        else :
            gc=0
        ts=request.form['Touchscreen']
        if ts == 'yes':
            ts=1
        else:
            ts=0
         
        dd=[ram,ddr,pn,pt,os,s,d,si,c,gc,ts]
        Xnew = np.array(dd).reshape((1,-1))
        prediction=model.predict(Xnew)
    
        output = round(prediction[0])

        return render_template('lap.html', prediction_text='The budget for your laptop is',upp=output+4000,low=output-4000)
        


if __name__ == '__main__':
    app.run(debug=True)


