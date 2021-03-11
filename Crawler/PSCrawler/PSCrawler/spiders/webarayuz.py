from flask import Flask,render_template,request,flash,url_for,redirect
from wtforms import Form,StringField,TextAreaField,validators,widgets,MultipleFileField,SelectField
from flask_wtf import FlaskForm
import json 
import os

class Filter(Form):
    min_price = StringField("Minimum Fiyat",validators=[validators.input_required()])
    max_price = StringField("Maksimum Fiyat",validators=[validators.input_required()])
    
class Site(FlaskForm):
    site = SelectField('Websiteleri', choices=["Tüm Siteler","evkur","teknosa","vatanbilgisayar","gittigidiyor"])   

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

with open('LGTV.json', encoding='utf-8') as fh:
    obj = json.load(fh)

for product in obj:
    if product['page'].split(".")[1] == "gittigidiyor":
        product['tv_Price'] = product['tv_Price'].split(',')[0]      

@app.route("/",methods = ["GET","POST"])
def index():
    
    form = Filter(request.form)
    form1 = Site()
    
    s = []
    if request.method == "POST":
        s = request.form.getlist("mycheckbox")
        return render_template("layout.html",answer = getir(form.min_price,form.max_price,s,form1),form = form,form1 = form1)
    else:
        return render_template("layout.html",answer = obj,form = form,form1 = form1)

def getir(minv,maxv,slist,formm):
    listt = []
    listt.clear()

    if(formm.site.data == "Tüm Siteler"):
    
        if len(slist) == 0:
            for item in obj:
                if int(item['tv_Price'].replace('.','').replace(',','')) <= int(maxv.data) and int(item['tv_Price'].replace('.','').replace(',','')) >= int(minv.data):
                    listt.append(item)
        else:
            for item in obj:
                if int(item['tv_Price'].replace('.','').replace(',','')) <= int(maxv.data) and int(item['tv_Price'].replace('.','').replace(',','')) >= int(minv.data) and size(slist,item):
                    listt.append(item)
    else:
        
        if len(slist) == 0:
            for item in obj:
                if int(item['tv_Price'].replace('.','').replace(',','')) <= int(maxv.data) and int(item['tv_Price'].replace('.','').replace(',','')) >= int(minv.data) and item['page'].split(".")[1] == formm.site.data:
                    listt.append(item)
        else:
            for item in obj:
                if int(item['tv_Price'].replace('.','').replace(',','')) <= int(maxv.data) and int(item['tv_Price'].replace('.','').replace(',','')) >= int(minv.data) and size(slist,item) and item['page'].split(".")[1] == formm.site.data:
                    listt.append(item)

    return listt

def size(ss,t):
    for k in ss:
        if t['tv_Name'][3:5] == k[0:2]:
            return True 
    return False

if __name__ == "__main__":
    app.run( )