from flask import Flask,render_template,redirect, request
import mlab
from mongoengine import Document, StringField, IntField

mlab.connect()

class GirlType(Document): #COLLECTION
    name = StringField()
    image = StringField()
    description = StringField()

# girl_type = GirlType(name = "Gái Tiểu Thư",
#                     image ="https://scontent.fhan4-1.fna.fbcdn.net/v/t1.0-9/21032766_687949738069098_2695562382087912876_n.jpg?oh=c4272a4774fbdc01f0baca18b488060f&oe=5A4E0DA7",
#                     description = "DESCRIPT: Hơi chảnh, Ít nói,Khó tiếp cận, Thích sạch sẽ, Thích Trai nhà giàu và nhiều tiền, hay mặc quần áo kín, gọn, đắt tiền")
# #girl_type.save()
# 1. connect to mlab
# 2.Add data
# 3.Get data for render_template

#create server
app = Flask(__name__)

g = [
{
'name' : 'Gái tiểu thư',
'image' : "https://scontent.fhan6-1.fna.fbcdn.net/v/t1.0-0/p480x480/21728252_875575869266847_4740553654170238597_n.jpg?oh=e4d59386a39b13dbe693dd5cff5857e5&oe=5A500E80",
'description' : '  __    Hơi chảnh, Ít nói,Khó tiếp cận, Thích sạch sẽ, Thích Trai nhà giàu và nhiều tiền, hay mặc quần áo kín, gọn, đắt tiền'
},
{
'name' : "Gái ngoan" ,
'image' : "https://scontent.fhan6-1.fna.fbcdn.net/v/t1.0-0/p480x480/21743360_875576375933463_3956243889743453113_n.jpg?oh=2162c3c9cd21370301b1e34595b7067b&oe=5A82B660",
'description' : "   __   Tính khá bình dân, trẻ như học sinh, gia như công sở, tính tình cẩn thẩn chăm học, hay đến thư viên, L'espace"
},
{
'name' : "Gái Hư" ,
'image' : "https://scontent.fhan6-1.fna.fbcdn.net/v/t1.0-9/19510343_831483063676128_451529134603326443_n.jpg?oh=349d673e41648ca4973d8cc34dba9de5&oe=5A3E09EE",
'description' : "   __   Thích vào bar "
}

]
#Configure
@app.route("/")
def index():
    return render_template("index.html", girl_type = g)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/school")
def schoolwebsite():
    return redirect ("http://techkids.vn/")
@app.route("/bmi")
def bmi():
    args = request.args
    weight = int(args["weight"])
    height = int(args["height"]) / 100
    bmi  = weight / (height **2)
    return "Your bmi is " + str(bmi)

@app.route('/bmi-calc')
def bmi_calc():
    return render_template("bmi_calc.html")
@app.route('/tutorial')
def tutorial():
    return render_template("tutorial.html")
#apprun
app.run(debug=True)
